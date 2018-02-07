class Error(Exception):
	'''Base Error.'''

	def __init__(self):
		self.error = 'Fatal error occured.'
		super().__init__(self.error)

class ArgError(Error):
	'''Argument Error.'''

	def __init__(self):
		self.error = 'Incorrect argument passed.'
		super().__init__(self.error)

class MissingArg(ArgError):
	'''Argument is missing.'''

	def __init__(self, arg):
		self.error = f'{arg} is a required argument that is missing.'
		super().__init__(self.error)

class InvalidArg(ArgError):
	'''Argument is invalid.'''

	def __init__(self, arg):
		self.error = f'{arg} is invalid.'
		super().__init__(self.error)

class HTTPError(Error):
	'''Error occured in HTTP.'''

	def __init__(self, code):
		self.error = f'An error occured. Status: {code}'
		super().__init__(self.error)

class Timeout(HTTPError):
	'''Connection timed out.'''

	def __init__(self):
		self.error = 'The connection timed out.'
		super().__init__(self.error)

class MissingData(Error):
	'''Missing data.'''

	def __init__(self, data):
		self.error = f'Value of {data} is missing.'