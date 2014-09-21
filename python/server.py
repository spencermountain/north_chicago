import os
import bing
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
        print "Resp={}".format(resp)
        #if resp.status_code != 200:
        #    print "Something went Wrong {}".format(resp.status_code)
        #    return '', False

        #if 'data' in resp:
        #    print resp['data']
        #    img = requests.get(
        #        'https://api.imgur.com/3/image/{}'.format(
        #            resp['data']))
        #    if 'link' in img:
        #        return img['link'], True
        return "hi"
