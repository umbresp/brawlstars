# RankedPlayer extends Box

(All methods and attributes of Box automatically belong to RankedPlayer.)

## Creating a RankedPlayer
The only way to create a RankedPlayer is to use get it from brawlstars.PlayerLeaderboard. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
lb = await client.get_player_leaderboard()
player = lb[0]
```

## RankedPlayer Attributes
| Variable | Description | Type |
|----------|-------------|------|
| tag | The player's tag. | string |
| name | The player's in-game name. | string |
| positionInLeaderboard | The rank of the player. | integer |
| trophies | How many trophies the player has. | integer |
| bandName | The name of the player's band. | string |
| expLevel | The player's experience level. | integer |

## RankedPlayer Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_id() | Returns the player's ID. | Id |

\*These methods can be awaited depending on if you created a Band through the sync or async client.