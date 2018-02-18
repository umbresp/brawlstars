# Errors

There are several different errors that you could get while trying to run code. Here's an exhaustive list of all of them.

## `brawlstars.errors.Error(Exception)`
This is the base error for all other BrawlStars errors. If this is the first error in the sequence, then either you've fucked up big time or there's a huge bug that all of us have somehow missed. Tl;Dr: You won't get this.

## `brawlstars.errors.ArgError(Error)`
This error means that something is wrong with an argument. As of release v0.2.6, the only argument that can be passed is `tag`. Check all your tags and make sure they're valid.

## `brawlstars.errors.MissingArg(ArgError)`
This one is pretty self explanatory. You're missing some data where you shouldn't be missing data, such as you tried to call `client.get_player()` instead of `client.get_player(tag)`.

## `brawlstars.errors.InvalidArg(ArgError)`
The argument you passed doesn't match what's valid for it. Example: You passed a `List` instead of a `String` for `tag`.

## `brawlstars.errors.HTTPError(Error)`
Something went wrong while requesting the data.

- 400: There was a bad request, maybe your tag seemed valid but didn't exist?
- 401: You have an invalid token.
- 404: The thing you are looking for doesn't exist.
- 418: I'm a teapot.
- 500: The server fucked up. Please report this in our discord server.
- 503: The API is temporarily unavailable. Please stand by.

## `brawlstars.errors.Timeout(Error):`
The connection timed out. Maybe your internet is slow or there's a lot of people requesting data at the moment.

## `brawlstars.errors.MissingData(Error):`
Something vital is missing in the response (e.g. a player without a tag, etc). These cannot be fixed but are instead our problem.