# BrawlStars

## Introduction
This is a python sync/async wrapper for the brawl stars API. Docs in progress!

## Installation
`pip install brawlstars` for the stable version

`pip install git+https://github.com/umbresp/brawlstars` for the beta version

## Examples

### With Synchronous Client
```py
import brawlstars

client = brawlstars.Client(token="your token here", timeout=5)
player = client.get_player(tag="Q8P2ULP")
print(player.name + " (#" + player.tag + ")") # Prints "Dreemurr (#Q8P2ULP)"
```
### With Asynchronous Client
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
