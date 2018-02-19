import requests
from box import Box
from .errors import Error, ArgError, MissingArg, InvalidArg, HTTPError, Timeout, MissingData

class Client:
    '''The client for brawl stars API.

    The client for brawl stars API.
    Methods are in snake_case.
    Attributes are in camelCase.
    '''
    def __init__(self, token, timeout=5):
        '''Creates an client.

        Creates an client.
        Automatically sets 4 attributes:

            __base_url: The base URL to make the request from.
            headers: Headers to pass when making the request.
            session: A requests.Session() object that represents the session.
            timeout: The timeout to wait before cancelling a request.
        '''
        self.__base_url = 'http://brawlstars-api.herokuapp.com/api/'
        self.timeout = timeout
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Umbresp | Python',
            'Authorization': token
        }
        self.get_profile = self.get_player

    def __str__(self):
        return f'Brawlstars Requests Client (timeout = {self.timeout}, session = {self.session})'

    def __repr__(self):
        return f'<BS Client timeout = {self.timeout} __base_url = {self.__base_url}>'

    def get_player(self, tag):

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            resp = self.sesssion.get(f'{self.__base_url}players/{tag}', headers=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except ValueError:
            raise MissingData('data')
        except:
            raise Timeout()


        data = Box(data)
        player = Player(data)
        return player

    def get_band(self, tag):

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            resp = requests.get(f'{self.__base_url}bands/{tag}', headers=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except ValueError:
            raise MissingData('data')
        except:
            raise Timeout()

        data = Box(data)
        band = Band(data)
        return band

class Player(Box):

    def __str__(self):
        return f'{self.name} #{self.tag}'

    def __repr__(self):
        return f'<Player tag = {self.tag} name = {self.name}'

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

    def __str__(self):
        return f'{self.name} #{self.tag}'

    def __repr__(self):
        return f'<Minimal Band tag = {self.tag} name = {self.name}'

    def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret

class Band(Box):

    def __str__(self):
        return f'{self.name} #{self.tag}'

    def __repr__(self):
        return f'<Band tag = {self.tag} name = {self.name}'

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

    def __str__(self):
        return f'{self.name}, position in clan {self.role}'

    def __repr__(self):
        return f'<Member role = {self.role} name = {self.name}'

    def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret

class Id(Box):

    def __str__(self):
        return f'{self.high}-{self.low}'

    def __repr__(self):
        return f'<ID high = {self.high} low = {self.low}'

class Brawler(Box):

    def __str__(self):
        return f'{self.name} ({self.trophies} trophies)'

    def __repr__(self):
        return f'<Brawler trophies = {self.trophies} name = {self.name}'