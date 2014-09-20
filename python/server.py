import os
import bing

from flask import Flask, request, render_template, jsonify, send_file, abort
import requests

app = Flask(__name__, static_url_path='')

class BadFileError(Exception):
    pass

@app.route('/upload', methods=['POST']):
def upload_to_imgur():
    '''
    takes a file and uploads it to imgur returning url
    '''
    if request.method == 'POST':
        fh = request.files.['image']
        print "Request has files {}".format(fh)
        resp = requests.post('https://api.imgur.com/3/image', {'image': fh})
        if resp.status_code != 200:
            print "Something went Wrong {}".format(resp.status_code)
            return '', False

        if 'data' in resp:
            img = requests.get(
                'https://api.imgur.com/3/image/{}'.format(
                    resp['data']))
            if 'link' in img:
                return img['link'], True
