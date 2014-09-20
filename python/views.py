import os
import hashlib
import ipdb

from flask import Flask, request, render_template, jsonify
# from app import app

UNSUPPORTED_MEDIA_STATUS = 415

app = Flask(__name__)

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
            filepath = os.path.join(cls.UPLOAD_DIR, filename)
            file_.save(filepath)
            return filepath
        else:
            raise BadFileError()

class QueryImage(object):
    def recognise(self):
        pass

@app.route('/', methods=['GET', 'POST'])
def index():
    print "HELLO WORLD??"
    return jsonify({"resp": "HELLO WORLD"})

@app.route('/upload', methods=['POST'])
def upload():
    print "got request: {}".format(request)
    print "has files: {}".format(request.files)
    file_ = request.files.get('image')

    # ipdb.set_trace()
    try:
        print "going to try to save"
        img = PhotoFilter.save(file_)
        return jsonify({"imgname": img})
    except BadFileError:
        return jsonify({"resp":"error"}), UNSUPPORTED_MEDIA_STATUS
