# Brawler extends Box

(All methods and attributes of Box automatically belong to Member.)

## Creating a Brawler
The only way to create a brawler is to use get it from brawlstars.Player. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
player = await client.get_player('Q8P2ULP')
brawlers = await player.get_brawlers()
brawler = brawlers[0]
```

## Brawler Attributes
| Variable | Description | Type |
|----------|-------------|------|
| highestTrophies | The highest trophies the brawler has ever been at. | integer |
| name | The name of the brawler. | string |
| trophies | The current trophies of the brawler. | integer |
| type | The type of the brawler (unknown what this does yet, and will always be 16) | integer |
| unk1 | Unknown value | integer |
| upgradesPower | How many upgrades the brawler has. Between 0 and 50. | integer |

## Brawler Methods
| Method | Description | Returns |
|--------|-------------|---------|

\*These methods can be awaited depending on if you created a Brawler through the sync or async client