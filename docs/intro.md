# Getting Started with BrawlStars

First, before you do anything, make sure brawlstars is updated to the latest stable version: `pip install -U brawlstars`
You should also have your API token handy with you. If you don't have one, hop in to our [discord server](https://discord.gg/6FtGdX7) and ask for one from either Zihad, Efesto, or me.

## Get a profile
Getting a profile is simple. First, import the brawlstars module:

```py
>>> import brawlstars
```

Now that you've imported the module, let's see what it can do.

```py
>>> print(dir(brawlstars))
['ArgError', 'AsyncClient', 'Band', 'Box', 'Brawler', 'Client', 'Error', 'HTTPError', 'Id', 
'InvalidArg', 'Member', 'MinimalBand', 'MissingArg', 'MissingData', 'Player', 'Timeout', 
'__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__github__', '__license__',
'__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__version__',
'aiohttp', 'asyncclient', 'asyncio', 'client', 'errors', 'requests']
```

This prints out all the attributes, methods, exceptions, and loaded modules in BrawlStars. 
(All the items starting with \_\_ are metadata, you don't need to worry about them for now.)
You also don't need to worry about the last 6 items, those are imported modules.

Let's create a Client (trying to create an instance of anything else will cause
an error because those objects do not have explicit `__init__` methods):

```py
>>> client = brawlstars.Client(token = "ABCDEFG", timeout = 5)
```
(We'll cover the asynchronous part of this later.)

The Client represents the connection to the API. It's necessary, or else you would have to
input your authorization in every request. It's also beneficial as you only have to open 1 session
instead of a new session every time you need some data. Let's see what the Client can give us:

```py
>>> print(dir(client))
['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'baseUrl',
'get_band', 'get_player', 'headers', 'timeout']
```

Here we see 5 important items in the Client. `baseUrl` is immutable; you cannot change the `baseUrl`.
`get_player` is the one we need, and it takes one argument- the player's tag.

```py
>>> player = client.get_player('Q8P2ULP')
```

Congratulations! You have now created a Player object, just as the title of this section told you to.

*But how do I get player statistics?*

Let's see what values and methods `Player` gives us.

```py
print(dir(player))
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'band', 
'box_it_up', 'brawlers', 'brawlersUnlocked', 'clear', 'copy', 'from_json', 'fromkeys', 'get', 
'highestTrophies', 'id', 'items', 'keys', 'name', 'pop', 'popitem', 'setdefault', 'showdownVictories',
'tag', 'to_dict', 'to_json', 'trophies', 'update', 'values', 'victories']
```

Since `Player` is a subclass of `Box`, many of the items are inherited from there. At this point you
should be able to see how to get the data you want, if you are still confused at this point, go learn Python.
Also, something I should mention, the methods for `Player` are not included in the directory. It's weird, I know.
If you really want to know what methods you can use for `Player`, go look in the documentation.

```py
>>> print(player.name)
Dreemurr
>>> print(player.trophies)
5093
```

## Errors and Exceptions
You may see a few errors that come up while following along with this tutorial (at least I hope you are).
Here's what most of them mean:

`brawlstars.errors.MissingArg`: You're missing something that needs to be present (most likely a player or band tag).

`brawlstars.errors.InvalidArg`: Something you've provided is invalid (most likely a player or band tag).

`brawlstars.errors.HTTPError`: Something went wrong in fetching the profile. 401 = You have an invalid token. 404 = 
Profile does not exist. 503 = The connection timed out.

`brawlstars.errors.Timeout`: The connection timed out. This isn't your fault, the API may just be down. If you do get
this error, however, make sure you scroll up in the error message. A lot of times this error happens after other errors
have occured.

`brawlstars.errors.MissingData`: Either the world is ending, in which case you should go hide in your bunker, or Zihad
forgot to include some vital information AGAIN!

## But wait! You promised to discuss the asynchronous client!

\*sighs\*... yes I did.

The asynchronous client, `brawlstars.AsyncClient`, functions exactly the same as `brawlstars.Client` except for two things:

1. Every single coroutine must be awaited or else you'll just get a bunch of responses about how you didn't await coroutines.
2. `brawlstars.AsyncClient.session` exists, but is pretty useless to you because it's immutable.

Don't believe me? Here's an example.

```py
import brawlstars
import asyncio

async def get_stats():
    client = brawlstars.AsyncClient(token="your token here", timeout=5)
    player = await client.get_player(tag="Q8P2ULP")
    print(player.name + " (#" + player.tag + ")") # Prints "Dreemurr (#Q8P2ULP)"

eventLoop = asyncio.get_event_loop()
eventLoop.run_until_complete(get_stats())
```

If you're confused by the asynchronous loop or what that means, go Google it. (This doesn't count as a difference
because it's explicitly stated that this client is asynchronous which should be obvious, given its name.)
