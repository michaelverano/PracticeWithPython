#!	/usr/local/bin python3
#	GoogleIt.py - Too lazy to open a web broswer? Type it in the fricken shell!

import logging, webbrowser, sys, pyperclip


if len(sys.argv) > 1:
	# Get address from the command line.
	address = ' '.join(sys.argv[1:])
	logging.debug('Address from command line is: ' + address) # Used for testing/debugging.
else:
	# Get address from clipboard.
	address = pyperclip.paste()
	logging.debug('Address from clipboard is: ' + address)

webbrowser.open('https://www.google.com/#q=' + address)
