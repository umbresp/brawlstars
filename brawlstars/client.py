import requests
from box import Box
from .errors import Error, ArgError, MissingArg, InvalidArg, HTTPError, Timeout, MissingData


class Client:
    """The client for brawl stars API.

    The client for brawl stars API.
    Methods are in snake_case.
    Attributes are in camelCase.
    """

    def __init__(self, token, timeout=5):
        """Creates an client.

        Creates an client.
        Automatically sets 4 attributes:

            _base_url: The base URL to make the request from.
            headers: Headers to pass when making the request.
            session: A requests.Session() object that represents the session.
            timeout: The timeout to wait before cancelling a request.
        """
        self._base_url = 'https://brawlapi.cf/api'
        self.timeout = timeout
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Brawlstars | Python',
            'Authorization': token
        }
        self.get_profile = self.get_player

    def __del__(self):
        """Safely destructs and closes the session."""
        self.session.close()

    def __str__(self):
        """Returns a string to print."""
        return 'Brawlstars Requests Client (timeout = ' + str(self.timeout) + ', session = ' + str(self.session) + ')'

    def __repr__(self):
        """Returns a string to eval."""
        return '<BS Client timeout = ' + str(self.timeout) + ' _base_url = ' + self._base_url + '>'

    def get_player(self, tag):
        """Gets a player.

        Gets a player with specified tag. If no tag is specified, the request will fail.
        If the tag is invalid, a brawlstars.InvalidTag will be raised.
        If the data is missing, a ValueError will be raised.
        If the connection times out, a brawlstars.Timeout will be raised.
        If the data was unable to be received, a brawlstars.HTTPError will be raised along with the
        HTTP status code.
        On success, will return a Player.
        """

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            resp = self.session.get(self._base_url + 'players/' + tag, headers=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except ValueError:
            raise MissingData('data')
        except Exception:
            raise Timeout()

        data = Box(data)
        player = Player(data)
        return player

    def get_band(self, tag):
        """Gets a band.

        Gets a band with specified tag. If no tag is specified, the request will fail.
        If the tag is invalid, a brawlstars.InvalidTag will be raised.
        If the data is missing, a ValueError will be raised.
        If the connection times out, a brawlstars.Timeout will be raised.
        If the data was unable to be received, a brawlstars.HTTPError will be raised along with the
        HTTP status code.
        On success, will return a Band.
        """

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            resp = requests.get(self._base_url + 'bands/' + tag, headers=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except ValueError:
            raise MissingData('data')
        except Exception:
            raise Timeout()

        data = Box(data)
        band = Band(data)
        return band

    def get_player_leaderboard(self):

        try:
            resp = requests.get(self._base_url + 'leaderboards/players', headers=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except ValueError:
            raise MissingData('data')
        except Exception:
            raise Timeout()

        data = Box(data)
        data = PlayerLeaderboard(data)
        return data

    def get_band_leaderboard(self):

        try:
            resp = requests.get(self._base_url + 'leaderboards/bands', headers=self.headers, timeout=self.timeout)
            if resp.status_code == 200:
                data = resp.json()
            elif 500 > resp.status_code > 400:
                raise HTTPError(resp.status_code)
            else:
                raise Error()
        except ValueError:
            raise MissingData('data')
        except Exception:
            raise Timeout()

        data = Box(data)
        data = BandLeaderboard(data)
        return data


class Player(Box):

    def __str__(self):
        return self.name + ' #' + self.tag

    def __repr__(self):
        return '<Player tag = ' + self.tag + ' name = ' + self.name + '>'

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
        except AttributeError:
            return None
        band = Box(band)
        band = MinimalBand(band)
        return band


class MinimalBand(Box):

    def __str__(self):
        return self.name + ' #' + self.tag

    def __repr__(self):
        return '<Minimal Band tag = ' + self.tag + ' name = ' + self.name + '>'

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
        return self.name + ' #' + self.tag

    def __repr__(self):
        return '<Band tag = ' + self.tag + ' name = ' + self.name + '>'

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
            member_list = self.bandMembers
        except AttributeError:
            return None
        members = []
        for i in member_list:
            thing = Box(i)
            thing = Member(thing)
            members.append(thing)

        return members


class Member(Box):

    def __str__(self):
        return self.name + ', position in clan ' + self.role

    def __repr__(self):
        return '<Member role = ' + self.role + ' name = ' + self.name + '>'

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
        return self.high + '-' + self.low

    def __repr__(self):
        return '<ID high = ' + self.high + ' low = ' + self.low + '>'


class Brawler(Box):

    def __str__(self):
        return self.name + ' (' + self.trophies + ' trophies)'

    def __repr__(self):
        return '<Brawler trophies = ' + self.trophies + ' name = ' + self.name + '>'


class PlayerLeaderboard(Box):

    def __str__(self):
        return 'Player Leaderboard'

    def __repr__(self):
        return '<Player Leaderboard>'

    def get_players(self):
        try:
            member_list = self.players
        except AttributeError:
            return None
        members = []
        for i in member_list:
            thing = Box(i)
            thing = RankedPlayer(thing)
            members.append(thing)

        return members


class RankedPlayer(Box):

    def __str__(self):
        return self.name + ' (#' + self.tag + '), ranked #' + self.positionInLeaderboard

    def __repr__(self):
        return '<RankedPlayer name = ' + self.name + ' tag = ' + self.tag + ' rank = ' + self.positionInLeaderboard + '>'

    def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret


class BandLeaderboard(Box):

    def __str__(self):
        return 'Band Leaderboard'

    def __repr__(self):
        return '<Band Leaderboard>'

    def get_bands(self):
        try:
            member_list = self.bands
        except AttributeError:
            return None
        members = []
        for i in member_list:
            thing = Box(i)
            thing = RankedBand(thing)
            members.append(thing)

        return members


class RankedBand(Box):

    def __str__(self):
        return self.name + ' (#' + self.tag + '), ranked #' + self.positionInLeaderboard

    def __repr__(self):
        return '<RankedBand name = ' + self.name + ' tag = ' + self.tag + ' rank = ' + self.positionInLeaderboard + '>'

    async def get_id(self):
        try:
            ret = self.id
        except AttributeError:
            return None
        ret = Box(ret)
        ret = Id(ret)
        return ret
