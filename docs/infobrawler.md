# InfoBrawler extends Box

(All methods and attributes of Box automatically belong to InfoBrawler.)

## Creating an InfoBrawler
The only way to create a InfoBrawler is to use get it from brawlstars.StaticData. Example:
```py
import brawlstars
data = brawlstars.StaticData()
brawler = data.get_brawler('shelly')
```

## InfoBrawler Attributes
| Variable | Description | Type |
|----------|-------------|------|
| name | The name of the brawler. | string |
| description | The brawler's description. | string |
| type | Ranged or melee. | string |
| tier | The rarity of the brawler. | string |
| speed | The speed of the brawler. | string |
| hitpoints | The base amount of HP the brawler has. | integer |
| image | A relative link to the image for the brawler. | string |
| thumb_image | A relative link to the thumb for the brawler. | string |
| link | A link to the api page about the brawler. | string |

## InfoBrawler Methods
| Method | Description | Returns |
|--------|-------------|---------|
