# Map extends Box

(All methods and attributes of Box automatically belong to Map.)

## Creating an Map
The only way to create a Map is to use get it from brawlstars.StaticData. Example:
```py
import brawlstars
data = brawlstars.StaticData()
map = data.get_map('skull_creek')
```

## Map Attributes
| Variable | Description | Type |
|----------|-------------|------|
| name | The name of the map. | string |
| description | The map's description. | string |
| link | A link to the api page about the map. | string |

## Map Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_mode() | Gets the mode the map belongs to. | Mode\* |

\*When creating a Mode with Map, the description will be unavailable.