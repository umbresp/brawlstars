import aiohttp
import asyncio
from box import Box
from .errors import *

class AsyncClient:

    def __init__(self, token, timeout=5):
        self.token = token
        self.baseUrl = 'https://api.clashofclans.com/v1/'
        self.session = aiohttp.ClientSession()
        self.timeout = timeout
        self.headers = {
            'Authorization': f'Bearer {token}'
        }

    def __del__(self):
        self.session.close()

    async def getPlayer(self, tag=None):
        if tag is None:
            raise MissingArg('tag')

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            async with self.session.get(f'{self.baseUrl}players/%23{tag}', timeout=self.timeout, headers=self.headers) as resp:
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

        data = Box(data)
        player = Player(data)
        return player

    async def getLeagues(self):
        try:
            async with self.session.get(f'{self.baseUrl}leagues', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()

        data = Box(data)
        leagues = []
        for i in range(data.items):
            league = League(data.items[i])
            leagues.append(league)

        return leagues

    async def getLeague(self, league):
        try:
            async with self.session.get(f'{self.baseUrl}leagues/{league}', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()

        data = Box(data)
        league = League(data)
        return league

    async def getLeagueSeasons(self, league):
        try:
            async with self.session.get(f'{self.baseUrl}leagues/{league}/seasons', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()
        thing = data['items'] # sorry
        seasons = []
        for i in range(len(thing)):
            temp = Box(thing[i])
            temp = GenericIDObject(temp)
            seasons.append(temp)
        return seasons

    async def getLeagueSeasonRankings(self, league, season):
        try:
            async with self.session.get(f'{self.baseUrl}leagues/{league}/seasons/{season}', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()
        thing = data['items'] # sorry
        rankings = []
        for i in range(len(thing)):
            temp = Box(thing[i])
            rankings = RankedPlayer(temp)
            rankings.append(temp)
        return rankings

    async def getLocations(self):
        try:
            async with self.session.get(f'{self.baseUrl}locations', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()

        thing = data['items'] # sorry
        locations = []
        for i in range(len(thing)):
            temp = Box(thing[i])
            temp = Location(temp)
            locations.append(temp)
        return locations

    async def getLocation(self, location):
        try:
            async with self.session.get(f'{self.baseUrl}locations/{location}', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()

        data = Box(data)
        location = Location(data)
        return location

    # TODO location clan rankings

    # TODO location player rankings

    # TODO location builder clan rankings

    # TODO location builder player rankings
    
    # TODO implement clan search

    async def getClan(self, tag=None):
        if tag is None:
            raise MissingArg('tag')

        tag = tag.strip("#")
        tag = tag.upper()

        try:
            async with self.session.get(f'{self.baseUrl}clans/%23{tag}', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()

        data = Box(data)
        clan = Clan(data)
        return clan

    async def getClanMembers(self, clantag):
        try:
            async with self.session.get(f'{self.baseUrl}clans/{clantag}/members', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()
        thing = data['items'] # sorry
        members = []
        for i in range(len(thing)):
            temp = Box(thing[i])
            temp = Player(temp)
            members.append(temp)
        return members

    async def getClanWarlog(self, clantag):
        try:
            async with self.session.get(f'{self.baseUrl}clans/{clantag}/warlog', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()
        thing = data['items'] # sorry
        logItems = []
        for i in range(len(thing)):
            temp = Box(thing[i])
            temp = WarlogItem(temp)
            logItems.append(temp)
        return logItems

    async def getClanWar(self, clantag):
        try:
            async with self.session.get(f'{self.baseUrl}clans/{clantag}/currentwar', timeout=self.timeout, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                elif 500 > resp.status > 400:
                    raise HTTPError(resp.status)
                else:
                    raise Error()
        except asyncio.TimeoutError:
            raise Timeout()

        data = Box(data)
        war = WarlogItem(data)
        return war

class Player(Box):

    async def getLeague(self):
        try:
            league = self.league
        except AttributeError:
            return None
        league = Box(league)
        league = League(league)
        return league

    async def getClan(self):
        try:
            clan = self.clan
        except AttributeError:
            return None
        clan = Box(clan)
        clan = Clan(clan)
        return clan

    async def getLegendStatistics(self):
        try:
            ls = self.legendStatistics
        except AttributeError:
            return None
        ls = Box(ls)
        ls = LegendStatistics(ls)
        return ls

    async def getAchievements(self):
        try:
            ac = self.achievements # i can't spell
        except AttributeError:
            raise MissingData('achievements')
        acs = []
        for i in ac:
            tempac = Box(i)
            tempac = Achievement(tempac)
            acs.append(tempac)
        return acs

    async def getTroops(self):
        try:
            troop = self.troops
        except AttributeError:
            raise MissingData('troops')
        troops = []
        for i in troop:
            temp = Box(i)
            temp = Troop(temp)
            troops.append(temp)
        return troops

    async def getHeroes(self):
        try:
            hero = self.heroes
        except AttributeError:
            return None
        heroes = []
        for i in hero:
            temp = Box(i)
            temp = Hero(temp)
            heroes.append(temp)
        return heroes

    async def getSpells(self):
        try:
            spell = self.spells
        except AttributeError:
            return None
        spells = []
        for i in spell:
            temp = Box(i)
            temp = Spell(temp)
            spells.append(temp)
        return spells

class League(Box):

    async def getIcons(self):
        try:
            iconUrls = self.iconUrls
        except:
            raise MissingData('iconUrls')
        iconUrls = Box(iconUrls)
        iconUrls = UrlList(iconUrls)
        return iconUrls

class Clan(Box):

    async def getLocation(self):
        try:
            location = self.location
        except:
            raise MissingData('location')
        location = Box(location)
        location = Location(location)
        return location

    async def getBadges(self):
        try:
            badgeUrls = self.badgeUrls
        except:
            raise MissingData('badgeUrls')
        badgeUrls = Box(badgeUrls)
        badgeUrls = UrlList(badgeUrls)
        return badgeUrls

    async def getMembers(self):
        try:
            memberList = self.memberList
        except:
            raise MissingData('memberList')
        members = []
        for i in memberList:
            temp = Box(i)
            temp = Player(temp)
            members.append(temp)
        return members

class LegendStatistics(Box):

    async def getCurrentSeason(self):
        try:
            currentSeason = self.currentSeason
        except:
            raise MissingData('currentSeason')
        currentSeason = Box(currentSeason)
        currentSeason = SeasonStatistic(currentSeason)
        return currentSeason

    async def getPreviousSeason(self):
        try:
            previousSeason = self.previousSeason
        except:
            raise MissingData('previousSeason')
        previousSeason = Box(previousSeason)
        previousSeason = SeasonStatistic(previousSeason)
        return previousSeason

    async def getBestSeason(self):
        try:
            bestSeason = self.bestSeason
        except:
            raise MissingData('bestSeason')
        bestSeason = Box(bestSeason)
        bestSeason = SeasonStatistic(bestSeason)
        return bestSeason

class Achievement(Box):
    pass

class Troop(Box):
    pass

class Hero(Box):
    pass

class Spell(Box):
    pass

class UrlList(Box):
    pass

class Location(Box):
    pass

class SeasonStatistic(Box):
    pass

class GenericIDObject(Box):
    pass

class RankedPlayer(Box):
    # Not sure how inheritence works in python so won't risk it

    async def getLeague(self):
        try:
            league = self.league
        except AttributeError:
            return None
        league = Box(league)
        league = League(league)
        return league

    async def getClan(self):
        try:
            clan = self.clan
        except AttributeError:
            return None
        clan = Box(clan)
        clan = Clan(clan)
        return clan

    async def getLegendStatistics(self):
        try:
            ls = self.legendStatistics
        except AttributeError:
            return None
        ls = Box(ls)
        ls = LegendStatistics(ls)
        return ls

    async def getAchievements(self):
        try:
            ac = self.achievements # i can't spell
        except AttributeError:
            raise MissingData('achievements')
        acs = []
        for i in ac:
            tempac = Box(i)
            tempac = Achievement(tempac)
            acs.append(tempac)
        return acs

    async def getTroops(self):
        try:
            troop = self.troops
        except AttributeError:
            raise MissingData('troops')
        troops = []
        for i in troop:
            temp = Box(i)
            temp = Troop(temp)
            troops.append(temp)
        return troops

    async def getHeroes(self):
        try:
            hero = self.heroes
        except AttributeError:
            return None
        heroes = []
        for i in hero:
            temp = Box(i)
            temp = Hero(temp)
            heroes.append(temp)
        return heroes

    async def getSpells(self):
        try:
            spell = self.spells
        except AttributeError:
            return None
        spells = []
        for i in spell:
            temp = Box(i)
            temp = Spell(temp)
            spells.append(temp)
        return spells

class WarlogItem(Box):

    async def getHomeClan(self):
        try:
            clan = self.clan
        except AttributeError:
            raise MissingData('clan')
        clan = Box(clan)
        clan = Clan(clan)
        return clan

    async def getOpponentClan(self):
        try:
            clan = self.opponent
        except AttributeError:
            raise MissingData('opponent')
        clan = Box(clan)
        clan = Clan(clan)
        return clan