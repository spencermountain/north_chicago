import os
import hashlib
import ipdb
import google

from flask import Flask, request, render_template, jsonify, send_file, abort

app = Flask(__name__, static_url_path='')

class BadFileError(Exception):
    pass

class PhotoFilter(object):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    UPLOAD_DIR = 'photos'

    @classmethod
    def ext_of(cls, file_):
        ext = os.path.splitext(file_.filename)[1].strip('.')
        print "got ext: {}".format(ext)
        return ext

    @classmethod
    def file_allowed(cls, file_):
        return cls.ext_of(file_) in cls.ALLOWED_EXTENSIONS

    @classmethod
    def allows(cls, file_):
        return file_ and cls.file_allowed(file_)

    @classmethod
    def hash(cls, file_):
        hash_ = hashlib.md5()
        hash_.update(file_.read())
        return hash_.hexdigest()

    @classmethod
    def save(cls, file_):
        print "trying to save..."
        if cls.allows(file_):
            print "is allowed"
            filename = "{}.{}".format(cls.hash(file_),
                                      cls.ext_of(file_))
            filepath = cls._qualify(filename)
            file_.save(filepath)
            return filepath
        else:
            raise BadFileError()

    @classmethod
    def _qualify(cls, name):
        return os.path.join(cls.UPLOAD_DIR, name)

    @classmethod
    def serve(cls, name):
        path = cls._qualify(name)
        if os.path.exists(path):
            return path
        else:
            raise BadFileError()


@app.route('/', methods=['GET', 'POST'])
def index():
    print "HELLO WORLD??"
    return jsonify({"resp": "HELLO WORLD"})

@app.route('/photos/<identifier>', methods=['GET'])
def serve(identifier):
    try:
        return send_file(PhotoFilter.serve(identifier))
    except BadFileError:
        abort(404)

@app.route('/upload', methods=['POST'])
def upload():
    '''
    uploads a photo and returns json object with key best_search value string
    corresponding to the result
    '''
    print "got request: {}".format(request)
    print "has files: {}".format(request.files)
    file_ = request.files.get('image')

    try:
        print "going to try to save"
        img_path = PhotoFilter.save(file_)
        print "got path: {}".format(img_path)
        query_image = google.QueryImage(img_path)
        resp = query_image.recognize()
        return jsonify({"best_search": resp})
    except BadFileError:
        return jsonify({"resp":"error"}), UNSUPPORTED_MEDIA_STATUS
