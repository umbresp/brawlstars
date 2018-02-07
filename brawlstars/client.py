import requests
from box import Box
from .errors import *

class Client:

    def __init__(self, timeout=5):
        self.baseUrl = 'http://brawl-stars.herokuapp.com/api/'
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Umbresp\'s BrawlStars Python Wrapper'
        }

    def __del__(self):
        pass

    def getPlayer(self, tag=None):
        if tag is None:
            raise MissingArg('tag')

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            resp = requests.get(f'{self.baseUrl}players/{tag}', params=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except:
            raise Timeout()

        if data['status']['error']:
            raise HTTPError(data['status']['code'])
            
        data = data['data']
        data = Box(data)
        player = Player(data)
        return player

class Player(Box):

    def getBand(self):
        try:
            band = self.band
        except AttributeError:
            return None
        band = Box(band)
        band = Band(band)
        return band

    def getStats(self):
        try:
            ls = self.stats
        except AttributeError:
            return None
        ls = Box(ls)
        ls = Stats(ls)
        return ls

    def getProfile(self):
        try:
            ls = self.profile
        except AttributeError:
            return None
        ls = Box(ls)
        ls = Profile(ls)
        return ls

class Band(Box):
    pass

class Stats(Box):
    pass

class Profile(Box):
    pass