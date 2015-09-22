#! 	Python3
#	filterSearch.py - a program that walks through the folder tree and searches 
#	for files with a certain file extension (.txt, .py, etc). 
#	Makes a new folder and copies the files from whatever location they are in.
#
#	Advanced TODO: Make this more modular. Especially the transition from searchFiles 
#	to newFolder functions.

import os, shutil

# Walk an entire folder tree searching for files.
def endsWith(fileType):
	if fileType.endswith('.py'):
		print('Python file searched.')
		searchFiles(fileType)
	elif fileType.endswith('.txt'):
		print('Text file searched.')
		searchFiles(fileType)
	else: 
		print('Not an option.')

def searchFiles(fileType):
	searched_files = []
	for folders, subfolders, filenames in os.walk(os.getcwd()):
		for items in filenames:
			if items.endswith(fileType):
				searched_files.append(items)

	print('Here are the searched files that have the ' + fileType + ' exension. \n' + str(searched_files))
	return searched_files

	# Make this modular in the future.
	answer = input('Would you like to put these in a new folder? > Y/n')
	if answer == 'Y' or answer.lower() == 'yes':
		newFolder(fileType)

	# TODO: Finish this function.
def newFolder(files):
	print(files)

if __name__ == '__main__':
	fileType = input('Do you want to search .py or .txt files? > ')
	endsWith(fileType)
	