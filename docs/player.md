# Player extends Box

(All methods and attributes of Box automatically belong to Player.)

## Creating a Player
The only way to create a player is to use get it from brawlstars.Client or brawlstars.AsyncClient. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
player = await client.get_player('Q8P2ULP')
```

## Player Attributes
| Variable | Description | Type |
|----------|-------------|------|
| brawlersUnlocked | How many brawlers the player has unlocked. | integer |
| highestTrophies | How many trophies the player has ever reached. | integer |
| name | The player's in-game name. | string |
| showdownVictories | How many wins the player has in Showdown. | integer |
| tag | The player's unique tag. | string |
| trophies | How many trophies the player currently has. | integer |
| victories | How many wins the player has in modes other than Showdown. | integer |

## Player Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_band() | Returns information about the player's band. | MinimalBand |
| get_brawlers() | Returns information about the player's brawlers. | List of Brawler |
| get_id() | Returns the player's ID. | Id |

\*These methods can be awaited depending on if you created a Player through the sync or async client.