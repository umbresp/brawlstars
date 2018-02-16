# AsyncClient

## Creating a AsyncClient:
`client = brawlstars.AsyncClient(*args, **kwargs)`
| Argument | Description | Type |
|----------|-------------|------|
| token | The authorization header to be passed to access the API. | string |
| timeout* | How long to wait for response. | integer |

\*optional

## Client Attributes
| Variable | Description | Type |
|----------|-------------|------|
| baseUrl* | Base URL to make requests to. | string |
| headers | Dictionary for headers to pass when making the request. Includes the token. | Dict |
| session* | The aiohttp session. | aiohttp.ClientSession |
| timeout | How long to wait for response. | integer |

\*immutable

## Client Methods
| Method | Description | Returns |
|--------|-------------|---------|
| await get_band(tag) | Get information about a band with specified tag. | Band |
| await get_player(tag) | Get information about a player with specified tag. | Player |
