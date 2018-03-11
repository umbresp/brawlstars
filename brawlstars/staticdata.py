import requests
from box import Box
from .errors import Error, ArgError, MissingArg, InvalidArg, HTTPError, Timeout, MissingData
import json


class StaticData:

    def __init__(self, timeout=5):
        self.timeout = timeout
        self._base_url = "https://brawlapi.axaygadekar.me/api/"

    def __str__(self):
        return 'BrawlStars StaticData Object'

    def __repr__(self):
        return '<BrawlStars StaticData Object>'

    def get_brawlers(self):
        try:
            resp = requests.get(self._base_url + 'brawlers', timeout=self.timeout)
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

        brawlers = []
        for brawler in data:
            brawler = Box(brawler)
            brawler = InfoBrawler(brawler)
            brawlers.append(brawler)

        return brawlers

    def get_brawler(self, name):
        brawlers = ['shelly', 'colt', 'nita', 'el_primo', 'dynamike',
                    'barley', 'bo', 'crow', 'spike', 'tara', 'mortis',
                    'bull', 'pam', 'piper', 'poco', 'ricochet', 'darryl',
                    'brock', 'jessie']

        if name.lower().replace(" ", "_") == "shelly":
            name = "shelley"  # fuck u axay u misspelled it
        if name.lower().replace(" ", "_") not in brawlers:
            raise InvalidArg('name')

        try:
            resp = requests.get(self._base_url + 'brawlers/' + name.lower().replace(" ", "_"), timeout=self.timeout)
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
        data = InfoBrawler(data)
        return data

    def get_modes(self):
        try:
            resp = requests.get(self._base_url + 'modes', timeout=self.timeout)
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

        modes = []
        for mode in data:
            mode = Box(mode)
            mode = Mode(mode)
            modes.append(mode)

        return modes

    def get_mode(self, name):
        modes = ['robo_rumble', 'boss_fight', 'showdown', 'bounty', 'smash_grab', 'heist', 'brawl_ball']
        sng = ['sng', 'smashngrab', 'smash_n_grab', 'smash_&_grab', 'smash&grab', 'smash_and_grab']
        if name.lower().replace(" ", "_") in sng:
            name = 'smash_grab'
        if name.lower().replace(" ", "_") not in modes:
            raise InvalidArg('name')

        try:
            resp = requests.get(self._base_url + 'modes/' + name.lower().replace(" ", "_"), timeout=self.timeout)
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
        data = Mode(data)
        return data

    def get_maps(self):
        try:
            resp = requests.get(self._base_url + 'maps', timeout=self.timeout)
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

        maps = []
        for map_ in data:
            map_ = Box(map_)
            map_ = Map(map_)
            maps.append(map_)

        return maps

    def get_map(self, name):
        maps = ['gg_corral', 'bandit_stash', 'kaboom_canyon', 'safe_zone', 'feast_famine',
                'skull_creek', 'death_valley', 'stormy_plains', 'calamity_canyon', 'star_gulch',
                'snake_prairie', 'shooting_star', 'outlaw_camp', 'groundhog_burrow', 'temple_ruins',
                'terracotta_square', 'cabbage_patch', 'bone_box', 'temple_cacatombs', 'deep_hollows',
                'hard_rock_mine', 'crystal_cavern', 'mushroom_cave', 'backyard_bowl', 'pinhole_punt',
                'triple_dribble', 'pachinko_park']
        ggc = ['gg_corral', 'g_g_corral', 'g._g._corral', 'g.g.corral']
        if name.lower().replace(" ", "_") in ggc:
            name = 'gg_corral'
        if name.lower().replace(" ", "_") not in maps:
            raise InvalidArg('name')

        try:
            resp = requests.get(self._base_url + 'maps/' + name.lower().replace(" ", "_"), timeout=self.timeout)
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
        data = Map(data)
        return data


class InfoBrawler(Box):

    def __str__(self):
        return 'InfoBrawler ' + self.name

    def __repr__(self):
        return '<InfoBrawler ' + self.name + '>'


class Mode(Box):

    def __str__(self):
        return 'Mode ' + self.name

    def __repr__(self):
        return '<Mode ' + self.name + '>'


class Map(Box):

    def __str__(self):
        return 'Map ' + self.name

    def __repr__(self):
        return '<Map ' + self.name + '>'

    def get_mode(self):
        mode = self.mode
        mode = Box(mode)
        mode = Mode(mode)
        return mode
