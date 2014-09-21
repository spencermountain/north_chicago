import os
import bing
import bloomberg
import pyimgur

from flask import Flask, request, render_template, jsonify, send_file, abort
import requests

app = Flask(__name__, static_url_path='')

class BadFileError(Exception):
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    print "Server up and running."
    return jsonify({"resp": "As you were."})

@app.route('/upload', methods=['POST'])
def upload_to_imgur():
    '''
    takes a file and uploads it to imgur returning url
    '''
    client_id = '66facd50284cdb5'

    if request.method == 'POST':
        fh = request.files['image']
        print "Request has files {}".format(fh)

        im = pyimgur.Imgur(client_id)
        resp = im.upload_image(fh, title="test")
        if not resp:
            print "Something went wrong with image upload"
            return jsonify({'code': 400, 'msg': "No image provided."})
        print "Uploaded the image to {}".format(resp.link)
        best_match = bing.QueryImage(resp.link).recognize()
        print "The best match for your image is {}".format(best_match)
        #bloomberg.data_aquisition(
        return jsonify({'code': 200, 'best_match': best_match})
