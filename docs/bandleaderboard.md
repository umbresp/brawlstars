# BandLeaderboard extends Box

(All methods and attributes of Box automatically belong to BandLeaderboard.)

## Creating a BandLeaderboard
The only way to create a BandLeaderboard is to use get it from brawlstars.Client or brawlstars.AsyncClient. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
lb = await client.get_band_leaderboard()
```

## BandLeaderboard Attributes
| Variable | Description | Type |
|----------|-------------|------|

## BandLeaderboard Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_bands() | Returns a list of bands in the leaderboard. | List of RankedBand |

\*These methods can be awaited depending on if you created a Band through the sync or async client.