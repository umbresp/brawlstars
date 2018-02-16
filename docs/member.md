# Member extends Box

(All methods and attributes of Box automatically belong to Member.)

## Creating a Member
The only way to create a member is to use get it from brawlstars.Band. Example:
```py
import brawlstars
client = brawlstars.AsyncClient('token here', '5')
band = await client.get_band('P9829')
members = await band.get_members()
member = members[0]
```

## Member Attributes
| Variable | Description | Type |
|----------|-------------|------|
| avatar | The member's avatar ID. | integer |
| expLevel | The member's experience level. | integer |
| name | The member's in-game name. | string |
| role | The member's role in the band. | string |
| trophies | How many trophies the member currently has. | integer |

## Member Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_id() | Returns the member's ID. | Id |

\*These methods can be awaited depending on if you created a Member through the sync or async client