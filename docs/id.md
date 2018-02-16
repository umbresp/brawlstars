# Id extends Box

(All methods and attributes of Box automatically belong to Member.)

## Creating a Id
The only way to create a member is to use get it from brawlstars.Player, brawlstars.Member, brawlstars.Band. or brawlstars.MinimalBand. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
player = await client.get_player('Q8P2ULP')
id = await player.get_id()
```

## Id Attributes
| Variable | Description | Type |
|----------|-------------|------|
| high | The first part of the ID. | integer |
| low | The second part of the ID. | integer |

## Id Methods
| Method | Description | Returns |
|--------|-------------|---------|

\*These methods can be awaited depending on if you created a Id through the sync or async client