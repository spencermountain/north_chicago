'''
Provides infastructure to take an image and turn it into the string associated
with the image
'''
import json
import urllib
import requests
from bs4 import BeautifulSoup
from tech_companies import companies
from sys import argv

UNSUPPORTED_MEDIA_STATUS = 415

companies = [c.lower() for c in companies]

class LocalReverseGoogleSearcher(object):
    def get(self, query_img):
        r = requests.get(
            'https://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl={}'.format(
                query_img.img_path))
        html = r.text
        soup = BeautifulSoup(html)
        entries = [el.find("a").text
                   for el in soup.find_all("div", class_="info")]

        print "got entries: {}".format(entries)
        for entry in [entry.lower() for entry in entries]:
            for company in companies:
                print "checking company: {}".format(company)
                if company in entry:
                    return company
                else:
                    print "{} doesn't match".format(company)

class QueryImage(object):
    BASE_URL_FMT = "http://payback.ml:5000/{}"
    def __init__(self, img_path):
        '''
        img_path : string representing the url of the image
        '''
        # self.img_path = self._qualify(img_path)
        self.img_path = "http://i.imgur.com/1QPXzNR.jpg"
        print "made path: {}".format(img_path)
        self.searcher = LocalReverseGoogleSearcher() # ReverseGoogleSearcher()

    def _qualify(self, partial_path):
        return self.BASE_URL_FMT.format(partial_path)

    def recognize(self):
        '''
        Recognizes an image from a url of the image and returns the associated
        string
        Requires the ReverseGoogleSearcher object
        '''
        resp = self.searcher.get(self)
        return resp


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
        results = urllib.urlopen("https://sender.blockspring.com/api_v1/blocks/5a1b66ef208007c51a45fda220dbe8db?api_key=774acd76d965921aa9a109a048c4b260", data).read()
        # results = urllib.urlopen(
        #     "https://sender.blockspring.com/api_v1/blocks/e84cf245c2bcf63" \
        #     "03ef7b501305ef14b?api_key={}".format(self.API_KEY),
        #     data).read()
        first_load = json.loads(results)['results']
        print "first load: {}".format(first_load)
        return json.loads(first_load)
