# Mode extends Box

(All methods and attributes of Box automatically belong to Mode.)

## Creating an Mode
The only way to create a Mode is to use get it from brawlstars.StaticData or brawlstars.StaticData.map\*. Example:
```py
import brawlstars
data = brawlstars.StaticData()
mode = data.get_mode('showdown')
```

## Mode Attributes
| Variable | Description | Type |
|----------|-------------|------|
| name | The name of the mode. | string |
| description | The mode's description. | string |
| link | A link to the api page about the mode. | string |

## Mode Methods
| Method | Description | Returns |
|--------|-------------|---------|

\*When creating a Mode with Map, the description will be unavailable.