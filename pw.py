#! python3.2
# pw.py - an insecure password locker program

import sys, pyperclip

PASSWORDS = {
	'main email': '!9mjrv0288',
	'spam email': 'elitefn28',
	'luggage': '12345'
	}

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)