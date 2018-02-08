import aiohttp
import asyncio
from box import Box
from .errors import *

class AsyncClient:
    '''The Asynchronous client for brawl stars API.

    The Asynchronous client for brawl stars API.
    Methods are in snake_case.
    Attributes are in camelCase.
    '''

    def __init__(self, token, timeout=5):
        self.baseUrl = 'https://brawl-stars.herokuapp.com/api/'
        self.session = aiohttp.ClientSession()
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Umbresp | Python (Async)',
            'Authorization': f'Bearer {token}'
        }

    def __del__(self):
        self.session.close()

    def __repr__(self):
        return f'<Asynchronous BS Client timeout = {self.timeout}>'

    async def get_player(self, tag=None):
        if tag is None:
            raise MissingArg('tag')

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            async with self.session.get(f'{self.baseUrl}players/{tag}', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()
        except Exception:
            raise InvalidArg('tag')

        if data['status']['error']:
            raise HTTPError(data['status']['code'])

        data = data['data']
        data = Box(data)
        player = Player(data)
        return player

class Player(Box):

    async def get_band(self):
        try:
            band = self.band
        except AttributeError:
            return None
        band = Box(band)
        band = Band(band)
        return band

    async def get_stats(self):
        try:
            ls = self.stats
        except AttributeError:
            return None
        ls = Box(ls)
        ls = Stats(ls)
        return ls

    async def get_profile(self):
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
