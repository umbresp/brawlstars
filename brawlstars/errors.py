class Error(Exception):
    """Base Error."""
    pass


class ArgError(Error):
    """Argument Error."""
    pass


class MissingArg(ArgError):
    """Argument is missing."""

    def __init__(self, error):
        self.error = error + ' is a required argument that is missing.'


class InvalidArg(ArgError):
    """Argument is invalid."""

    def __init__(self, error):
        self.error = error + ' is invalid.'


class HTTPError(Error):
    """Error occured in HTTP."""

    def __init__(self, code):
        self.error = 'An error occurred. Status: ' + code


class Timeout(Error):
    """Connection timed out."""

    def __init__(self):
        self.error = 'The connection timed out.'


class MissingData(Error):
    """Missing data."""

    def __init__(self, data):
        self.error = 'Value of ' + data + ' is missing.'
