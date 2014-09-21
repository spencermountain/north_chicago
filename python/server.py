import os
import bing
import json
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
    takes a file and uploads it to imgur returning a json dictionary containing
    1. the code, 2. the string, best_match, and 3. the "booty", a json dictionary
    of all the information we deem important to return
    '''
    client_id = '66facd50284cdb5'

    if request.method != 'POST':
        print "You're using this endpoint wrong, its a POST"
        return jsonify({'code': 400, 'message': "Its a POST"})

    fh = request.files['image']
    im = pyimgur.Imgur(client_id)
    resp = im.upload_image(fh, title="test")

    if not resp:
        print "Something went wrong with image upload"
        return jsonify({'code': 400, 'message': "No image provided."})

    print "Uploaded the image to {}".format(resp.link)
    best_match = bing.QueryImage(resp.link).recognize()

    best_match, ok = bing.QueryImage(resp.link).recognize()
    if not ok:
        print "Stupid Bing"
        return jsonify({'code': 500, 'message': "Sorry, no matches were found. "\
                        "Please try to take a clearer picture."})
    print "The best match for your image is {}".format(best_match)

    json_data = json.loads(bloomberg.return_data(best_match))
    if not json_data['status']:
        print "Most likely you're searching a company that is not public"
        return jsonify({'code': 400, 'message': json_data['error']})

    return jsonify({'code': 200, 'best_match': best_match, 'booty': json_data})
