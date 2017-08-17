#This is a class for handling ANSI codes 
#Link to the Wikipedia site: https://en.wikipedia.org/wiki/ANSI_escape_code


class ANSI:
	#Miscellaneous
	escape = '\033'
	
	#Colors
	red = escape + '[31m'
	green = escape + '[32m'
	yellow = escape + '[33m'
	blue = escape + '[34m'
	magenta = escape + '[35m'
	cyan = escape + '[36m'
	white = escape + '[37m'
	default = escape + '[39m'
	redB = escape + '[41m'
	greenB = escape + '[42m'
	yellowB = escape + '[43m'
	blueB = escape + '[44m'
	magentaB = escape + '[45m'
	cyanB = escape + '[46m'
	whiteB = escape + '[47m'
	defaultB = escape + '[49m'


	#Move Cursor
	def left(self, count):
		return escape + '[%dD' % (count)

	def up(self, count):
		return escape + '[%dA' % (count)

	def right(self, count):
		return escape + '[%dC' % (count)

	def down(self, count):
		return escape + '[%dB' % (count)

	#Move cursor to a specific location

	def pos(self, posX, posY):
		return escape + '[%d;%dF' % (posX, posY)