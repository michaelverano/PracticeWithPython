#!	testFileCreator.py
#	testFileCreator.py - used to create files with a .txt file extension for testing with python proejects.

import os

def createFiles():
	pass

def createDirectory():
	newDirectory = input('What is the name of the directory you want to make? > ')
	test = os.mkdir(os.getcwd() + '/' + str(newDirectory))

if __name__ == '__main__':
	import directoryExplorer
	createDirectory() # for testing purposes onlyself.