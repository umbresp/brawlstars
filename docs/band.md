# Band extends Box

(All methods and attributes of Box automatically belong to Band.)

## Creating a Band
The only way to create a player is to use get it from brawlstars.Client or brawlstars.AsyncClient. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
band = await client.get_band('P9829')
```

## Band Attributes
| Variable | Description | Type |
|----------|-------------|------|
| bandDescription | The description in the Band's information box. | string |
| bandMembersCount | How many members are in the band. | integer |
| bandRequiredTrophies | How many trophies you need to join the band. | integer |
| bandTrophies | How many trophies the band has. | integer |
| name | The name of the band. | string |
| status | Whether the band is Invite Only, Open, or Closed. | string |
| tag | The band's unique tag. | string |

## Band Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_players() | Returns a list of members in the band. | List of Member |
| get_id() | Returns the band's ID. | Id |

\*These methods can be awaited depending on if you created a Band through the sync or async client.