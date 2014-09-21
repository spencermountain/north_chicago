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

class BingSearcher(object):
    def get(self, query_img):
        r = requests.get(
            'https://www.bing.com/images/searchbyimage?'\
            'FORM=IRSBIQ&cbir=sbi&imgurl={}'.format(query_img.img_path))
        html = r.text
        soup = BeautifulSoup(html)
        entries = [el.find("a").text
                   for el in soup.find_all("div", class_="info")]

        print "got entries: {}".format(entries)
        for entry in [entry.lower() for entry in entries]:
            print entry
            for company in companies:
                print "checking company: {}".format(company)
                if company in entry:
                    return company
                else:
                    print "{} doesn't match".format(company)


class QueryImage(object):
    def __init__(self, img_path):
        '''
        img_path : string representing the url of the image
        '''
        self.img_path = img_path #on imgur!
        print "made path: {}".format(img_path)
        self.searcher = BingSearcher()

    def recognize(self):
        '''
        Recognizes an image from a url of the image and returns the associated
        string
        Requires the ReverseGoogleSearcher object
        '''
        resp = self.searcher.get(self)
        return resp
