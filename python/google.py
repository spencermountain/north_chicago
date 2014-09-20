'''
Provides infastructure to take an image and turn it into the string associated
with the image
'''
import json
import urllib
from sys import argv

UNSUPPORTED_MEDIA_STATUS = 415

class QueryImage(object):
    BASE_URL_FMT = "payback.ml:5000/{}"
    def __init__(self, img_path):
        '''
        img_path : string representing the url of the image
        '''
        self.img_path = self._qualify(img_path)
        print "made path: {}".format(img_path)
        self.searcher = ReverseGoogleSearcher()

    def _qualify(self, partial_path):
        return self.BASE_URL_FMT.format(partial_path)

    def recognize(self):
        '''
        Recognizes an image from a url of the image and returns the associated
        string
        Requires the ReverseGoogleSearcher object
        '''
        resp = self.searcher.get(self)
        return resp['best_search']


class ReverseGoogleSearcher(object):
    API_KEY = '1d27fd4078cf840d5544cf943e642e9a'

    def get(self, image):
        '''
        __Input__
        image: QueryImage with a url of an image

        __Output__
        json object with fields 'best_search': string
        and 'direct_matches': list of strings
        '''
        data = urllib.urlencode({'image_url': image.img_path})
        print "sending data: {}".format(data)
        results = urllib.urlopen(
            "https://sender.blockspring.com/api_v1/blocks/e84cf245c2bcf63" \
            "03ef7b501305ef14b?api_key={}".format(self.API_KEY),
            data).read()
        first_load = json.loads(results)['results']
        return json.loads(first_load)
