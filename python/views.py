import os
import hashlib
import ipdb
import bing
import flickrapi

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
        file_.seek(0)
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
    print "Server up and running."
    return jsonify({"resp": "As you were."})

@app.route('/photos/<identifier>', methods=['GET'])
def serve(identifier):
    print "serving! for {}".format(identifier)
    try:
        return send_file(open(PhotoFilter.serve(identifier)))
    except BadFileError:
        abort(404)

@app.route('/upload', methods=['POST'])
def upload():
    '''
    uploads a photo and returns json object with key best_search value string
    corresponding to the result
    To upload photos to flickr, POST to https://up.flickr.com/services/upload/ with
    photo: <file>
    other stuff optional
    API key: 5a825e3fa13537b8afb6c437f4472a3a
    '''
    print "got request: {}".format(request)
    print "has files: {}".format(request.files)
    file_ = request.files.get('image')
    api_key = '5a825e3fa13537b8afb6c437f4472a3a'
    api_secret = 'd66a167af0701cfc'
    img_path = ''
    flickr = flickerapi.FlickrAPI(api_key, api_secret, format='json')


    (token, frob) = flickr.get_token_part_one(perms='write')
    if not token:
        raw_input('Press ENTER after you authorize this program')
    flickr.get_token_part_two((token, frob))
    #def callback(progress, done):
    #    if done:
    #        print "Upload finished to img_path={}".format(img_path)
    #   else:
    #        print "Upload {}% completed".format(progress)

    resp = flickr.upload(file_)
    #callback, title, description, tags, is_public, is_family, content_type, hidden, format='rest')
    print resp
    # try:
    #     session.post('https://up.flickr.com/services/upload/', {'photo': file_})
    #     img_path =

    #     print "got path: {}".format(img_path)
    #     query_image = bing.QueryImage(img_path)
    #     resp = query_image.recognize()
    #     return jsonify({"best_search": resp})
    # except BadFileError:
    #     return jsonify({"resp":"error"}), 415
