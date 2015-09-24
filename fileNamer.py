#!	python3
#!	fileNamer.py - takes a user input regular expression and searches for files of that expresion inside a folder.
#	Once a regular expression for a file has been found, the file prompts the user to change the name of that file.

import os, re, shutil

def fileNamer():
	print('fileNamer.py searches for files in a folder and lets you change the name.')

	searchFor = input('What files would you like to search? > ')
	regular_expression = re.compile(searchFor)
	directoryItems = next(os.walk(os.getcwd()))[2] # All of the files in the current directory are in a list.

	searchResults = re.findall(regular_expression, searchFor)

	# cycle through all the items on the program. Return the files that match the regular expression.
	for items in directoryItems:
		if  searchResults:
			print('Here is an item that matches your result... ' + items)
			print('Would you like to change the name?')
			YayOrNay = input('y to change, [ENTER] for no. > ')

			if YayOrNay.lower() == 'y': # replace with the new name.
				print('What would you like to change the name to?')
				newName = input('> ')

				print('\n ' + items + ' file name was changed to ' + newName + '\n')
				os.rename(items, newName)

	print('No more file names that match your search.')

if __name__ == '__main__':
	import directoryExplorer
	directoryExplorer.directoryExplorer(os.getcwd())
	#os.chdir(os.getcwd()+'/fileNamer test/') # for testing porpoises.

	fileNamer()