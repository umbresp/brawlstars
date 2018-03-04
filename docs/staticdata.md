# StaticData
StaticData is an object which contains all the static info about the game (in progress). Credit for the descriptions goes to axaygadekhar.

## Creating a StaticData
`data = brawlstars.StaticData(*args, **kwargs)`

| Argument | Description | Type |
|----------|-------------|------|
| timeout* | How long to wait for response. | integer |

\*optional

## StaticData Attributes
| Variable | Description | Type |
|----------|-------------|------|
| \_base\_url* | Base URL to make requests to. | string |
| timeout | How long to wait for response. | integer |

\*immutable

## StaticData Methods
| Method | Description | Returns |
|--------|-------------|---------|
| get_brawlers() | Get information about all the brawlers. | List of InfoBrawler\* |
| get_brawler(name) | Get information about a brawler. | InfoBrawler\* |
| get_maps() | Get information about all the maps. | List of Map |
| get_map(name) | Get information about a map. | Map |
| get_modes() | Get information about all the modes. | List of Mode |
| get_mode(name) | Get information about a mode. | Mode |

\*Not to be confused with Brawler.