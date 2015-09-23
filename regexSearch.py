#! python3 
# regexSearch.py - opens all .txt files in a folder and searches for any line that matches any 
#					user - supplied regular expression. Results printed on the screen.

# FUTURE TO DO: Can I make this into a GUI?
# FUTURE TODO: Open all non-binary files instead of just .txt extensions.


import re, os

# Navigate the operating system to find the directories.
def folderFinder(folder_location):
	current_directory = os.getcwd().split(os.path.sep)[1:] # List starting from second point to remove root.
	if folder_location in current_directory:
		# Move down a directory
		new_directory = ''
		for items in current_directory:
			if items == folder_location:
				new_directory += '/' + items
				break
			else:
				new_directory += '/' + items
		os.chdir(new_directory)
	else:
		os.chdir(folder_location)

	print('This is the current directory: ' + os.getcwd())

	intro()

# Opens files in the directory and searches them for the regex and outputs which files have it on the screan.
def fileCrawler(): # Meat of the project right hurr!
	print('python file or a text file?')
	whatFileType = input('.txt or .py: ')
	textRegex = re.compile(whatFileType)
	options = ['.py', '.txt']
	if whatFileType not in options:
		print('that is not an option.')
		fileCrawler()
	
	print('What would you like to search?')
	inputRegex = re.compile(input('> ')) # Turn into an input, later.
	

	no_Match = True

	# TODO: make program open files in the current directory.
	txtFiles = []
	for items in os.listdir():
		if os.path.isfile(items):
			if textRegex.search(items):
				txtFiles.append(items)

	for items in txtFiles:
		openFile = open(items)
		readFile = openFile.read()
		
		if inputRegex.search(readFile):
			no_Match = False
			print('There is a match: ' + str(items)) 

	if no_Match == True:
		print('There\'s no match!')

def intro():
	# Lists folders and asks what folder do you want to go to?
	print('\n\n\n\n\n\n\n\n\n\n\nCurrent folder: ' + str(os.getcwd()))	
	print('What folder do you want to search? Type "stay" to search current folder.') # search what folder.
	print('Move backwards :' + str(os.getcwd().split(os.path.sep)) + '\n')
	folders_ahead = []
	for items in os.listdir():
		if os.path.isdir(items):
			folders_ahead.append(items)
	print('Move forwards: ' + str(folders_ahead))

	move_folder = input('> ') 

	# Algo for moving to different functions or staying in this function.
	if move_folder in os.getcwd().split(os.path.sep) or move_folder in folders_ahead:
		
		if move_folder == '':
			print('Yeah, uh... no. It\'s best you don\'t go to root. :\ \nNothing against you or anything. (We just don\'t think you\'re that good yet.)')
			# intro()
		else:
			
			folderFinder(move_folder)
	elif move_folder == 'stay':
		fileCrawler() 

		# Go to fileCrawler

	else:
		print('These are not options.')
		intro()	

intro()
#fileCrawler()