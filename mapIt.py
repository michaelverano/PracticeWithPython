#!	mapIt.py
#	Launches as map in the browser using an address from the
#	command line or the clipboard.

import webbrowser, sys, logging, pyperclip

# to DEBUG this program.
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s' )
logging.disable(logging.CRITICAL) # turns debug mode off

if len(sys.argv) > 1:
	# Get address from the command line.
	address = ' '.join(sys.argv[1:])
	logging.debug('Address from command line is: ' + address) # Used for testing/debugging.
else:
	# Get address from clipboard.
	address = pyperclip.paste()
	logging.debug('Address from clipboard is: ' + address)

# TODO: Get address from the clipboard.

webbrowser.open('https://www.google.com/maps/place/' + address)
