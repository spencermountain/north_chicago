'''
Given the string called best search strip it to something searchable with the
Bloomberg API then
'''

class ImageType(object):
    '''
    Images are either Flags or Logos
    '''
    keywords = ['sign', 'logo', 'flag', 'app', 'icon']
    def __init__(self, best_search):
        self.best_search = best_search
        self.typ = decide_type()
        self.query = condense()
