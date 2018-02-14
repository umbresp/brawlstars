import requests
from box import Box
from .errors import *

class Client:
    '''The client for brawl stars API.

    The client for brawl stars API.
    Methods are in snake_case.
    Attributes are in camelCase.
    '''
    def __init__(self, token, timeout=5):
        self.baseUrl = 'http://brawlstars-api.herokuapp.com/api/'
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Umbresp | Python',
            'Authorization': token
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


        data = Box(data)
        player = Player(data)
        return player

    def get_band(self, tag=None):
        if tag is None:
            raise MissingArg('tag')

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            resp = requests.get(f'{self.baseUrl}bands/{tag}', params=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except:
            raise Timeout()

        data = Box(data)
        band = Band(data)
        return band

class Player(Box):

    def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret

    def get_brawlers(self):
        try:
            brawlers = self.brawlers
        except AttributeError:
            return None

        something = []
        for brawler in brawlers:
            thing = Box(brawler)
            thing = Brawler(thing)
            something.append(thing)

        return something

    def get_band(self):
        try:
            band = self.band
        except AttributError:
            return None
        band = Box(band)
        band = MinimalBand(band)
        return band


class MinimalBand(Box):

    def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret

class Band(Box):

    def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret

    def get_members(self):
        try:
            memberList = self.bandMembers
        except AttributError:
            return None
        members = []
        for i in memberList:
            thing = Box(i)
            thing = Member(thing)
            members.append(thing)

        return members

class Member(Box):

    def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret

class Id(Box):
    pass

class Brawler(Box):
    pass
