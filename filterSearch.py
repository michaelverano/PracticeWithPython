#! 	Python3
#	filterSearch.py - a program that walks through the folder tree and searches 
#	for files with a certain file extension (.txt, .py, etc). 
#	Makes a new folder and copies the files from whatever location they are in.
#
#	Advanced TODO: Make this more modular. Especially the transition from searchFiles 
#	to newFolder functions.

import os, shutil, pprint

# Walk an entire folder tree searching for files.
def endsWith(fileType):
	if fileType.endswith('.py'):
		print('Searching for Python files. Wait one momment...')
		searchFiles(fileType)
	elif fileType.endswith('.txt'):
		print('Searching for Text files. Wait one moment...')
		searchFiles(fileType)
	else: 
		print('Not an option.')

def searchFiles(fileType):
	searched_files = []
	for folders, subfolders, filenames in os.walk(os.getcwd()):
		for items in filenames:
			if items.endswith(fileType):
				# combine the filename with its path.
				full_name = os.path.join(folders, items)				
				searched_files.append(full_name)
	#pprint.pprint(searched_files) # test

	pprint.pprint('Here are the searched files that have the ' + fileType + ' exension. \n' + str(searched_files))

	# Make this modular in the future.
	answer = input('Would you like to put these in a new folder? > Y/n ')
	if answer == 'Y' or answer.lower() == 'yes':
		newFolder(searched_files, fileType)

	# TODO: Finish this function.
def newFolder(files, fileType):
	# files is a list, fileType is a string.
	# Check to see if a new folder exists and then creats a new folder and copies files listed in the 
	# searched_files list. 
	
	# Check to see if the folder exists.
	number = 1
	while True:
		createdFolder = 'Searched_' + fileType + '_files_' + str(number)
		if not os.path.exists(createdFolder):
			break
		number = number + 1
		#print(createdFolder) # for testing purposes

	# Make the folder.
	newFolderName = os.getcwd() + '/' +createdFolder
	#print(newFolderName) # for testing purposes.
	print('Making a new folder in ' + os.getcwd() + ' called\n ' + createdFolder)
	os.mkdir(newFolderName)

	# Add the searched files in the folder.
	print('Adding the ' + fileType + 's in ' + newFolderName)
	for items in files:
		shutil.copy(items, newFolderName)

if __name__ == '__main__':
	fileType = input('Do you want to search .py or .txt files? > ')
	endsWith(fileType)
	#newFolder(['files.txt', 'files2.txt'], '.txt') # for testing purposes