import requests
from box import Box
from .errors import *

class Client:
    '''The client for brawl stars API.

    The client for brawl stars API.
    Methods are in snake_case.
    Attributes are in camelCase.
    '''
    def __init__(self, timeout=5):
        self.baseUrl = 'http://brawl-stars.herokuapp.com/api/'
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Umbresp | Python'
        }

    def __del__(self):
        pass

    def __repr__(self):
        return f'<BS Client timeout = {self.timeout}>'

    def get_player(self, tag=None):
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

    def get_band(self):
        try:
            band = self.band
        except AttributeError:
            return None
        band = Box(band)
        band = Band(band)
        return band

    def get_stats(self):
        try:
            ls = self.stats
        except AttributeError:
            return None
        ls = Box(ls)
        ls = Stats(ls)
        return ls

    def get_profile(self):
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