# RankedBand extends Box

(All methods and attributes of Box automatically belong to RankedBand.)

## Creating a RankedBand
The only way to create a RankedBand is to use get it from brawlstars.BandLeaderboard. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
lb = await client.get_band_leaderboard()
band = lb[0]
```

## RankedBand Attributes
| Variable | Description | Type |
|----------|-------------|------|
| tag | The band's tag. | string |
| name | The band's in-game name. | string |
| positionInLeaderboard | The rank of the band. | integer |
| trophies | How many trophies the band has. | integer |
| membersCount | How many people are in the band. | integer |

## RankedBand Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_id() | Returns the band's ID. | Id |

\*These methods can be awaited depending on if you created a Band through the sync or async client.