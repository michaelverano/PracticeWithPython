#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: 	python mcb.pyw save <keyword> - Saves clipboard to keyword.
#			python mcb.pyw <keyword> - loads keyword to clipboard.
#			python mcb.pyw list - Loads all keywords to clipboard.
#			python mcb.pyw delete <keyword> - Deletes the keyword on mcb.
#			python mcb.pyw delete	- Deletes everything

import shelve, pyperclip, sys, os

mcbShelf = shelve.open('mcb') # Note, this creates a dictionary, but outputs a list of the keys.

#TODO: Save Clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
#TODO: Write a delete <keyword> command.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	
	if sys.argv[2].lower() == 'file':
		print('Are you sure you want to delete the file?')
		answer = input('Y/n :')

		if answer == 'Y' or answer.lowercase() == 'yes':
			os.remove('mcb.db')
			exit()
		elif answer == 'n' or answer.lowercase() == 'no':
			print('Shits not in, yo')
			
	if sys.argv[2].lower() in mcbShelf:
		del mcbShelf[sys.argv[2]]

		pyperclip.copy(str(list(mcbShelf.keys())))

	else:
		print('shits not in, yo!')

elif len(sys.argv) == 2:
	#TODO: List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	#TODO: Write a delete all command.
	elif sys.argv[1].lower() == 'delete':
		print('Do you want to delete your saved clipboard items?') #Safety measure
		answer = input('Y/n : ')
		if answer == 'Y' or answer.lower() == 'yes':
			print('Deleting all the things!')
			# Deletes all the things by calling the dictionary
			for items in mcbShelf:
				del mcbShelf[items]

			pyperclip.copy(str(list(mcbShelf.keys())))
			exit()
		if answer == 'n' or answer.lower() == 'no':
			print('Not deleting all the things! :(')
			exit()
		else:
			print('That\'s not an option')
			
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	else:
		print('stuff')

"""
#TODO: Write a delete file command.
"""