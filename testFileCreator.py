#!	testFileCreator.py
#	testFileCreator.py - used to create files with a .txt file extension for testing with python proejects.

import os, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # For debugging purposes. Turn debug mode off by uncommenting.

def createDirectory():
	newDirectory = input('What is the name of the directory you want to make? > ')
	os.mkdir(os.getcwd() + '/' + str(newDirectory))
	os.chdir('./'+str(newDirectory))
	logging.debug('Your current directory is now ' + str(os.getcwd()))

def createFiles():
	print('How many files do you want to make?')

	# Future Todo: Make this a failsafe system that checks number to be int, or else it will loop again.
	# Try this again when you relearn the try/exception/else again.
	number = int(input('> '))

	for x in range(1, number+1):
		open('file_'+str(x)+'.txt', 'w')
		logging.debug('Creating file ' + str(x))

	print(str(number) + ' files created.')

if __name__ == '__main__':
	import directoryExplorer
	print('Do you want to create these new files in a specific directory?')
	answer = input('> ')

	if answer.lower() == 'yes':
		directoryExplorer.directoryExplorer(os.getcwd())
	
	createDirectory()
	createFiles()