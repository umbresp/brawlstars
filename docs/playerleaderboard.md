# PlayerLeaderboard extends Box

(All methods and attributes of Box automatically belong to PlayerLeaderboard.)

## Creating a PlayerLeaderboard
The only way to create a PlayerLeaderboard is to use get it from brawlstars.Client or brawlstars.AsyncClient. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
lb = await client.get_player_leaderboard()
```

## PlayerLeaderboard Attributes
| Variable | Description | Type |
|----------|-------------|------|

## PlayerLeaderboard Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_players() | Returns a list of players in the leaderboard. | List of RankedPlayer |

\*These methods can be awaited depending on if you created a Band through the sync or async client.