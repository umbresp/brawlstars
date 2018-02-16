# MinimalBand extends Box

(All methods and attributes of Box automatically belong to MinimalBand.)

## Creating a MinimalBand
The only way to create a minimal band is to use get it from brawlstars.Player. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
player = await client.get_player('Q8P2ULP')
band = await player.get_band()
```

## MinimalBand Attributes
| Variable | Description | Type |
|----------|-------------|------|

## MinimalBand Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_id() | Returns the band's ID. | Id |

\*These methods can be awaited depending on if you created a MinimalBand through the sync or async client.