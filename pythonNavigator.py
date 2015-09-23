#! 	python3
# 	pythonNavigator.py - Navigate your OS with this program!

import os


def pythonNavigator():
	print('\n\n\nThis is the current directory: ' + os.getcwd())
	print('Available folders moving back: ' + str(os.getcwd().split(os.path.sep)[1:]))
	directories = []
	for items in os.listdir():
		if os.path.isdir(items):
			directories.append(items)
	print('Curent directories in this directory: ' + str(directories))

	navigate = input('\n\n\nWhere do you want to go? : ')

	address = ''
	if navigate in os.getcwd(): # Move backwards in directory
		for items in os.getcwd().split(os.path.sep)[1:]:
			address += '/' + str(items)
			if items == navigate:
				break

		os.chdir(address)
		pythonNavigator()
	elif navigate in directories: # Move forwards in directory.
		for items in os.getcwd().split(os.path.sep)[1:]:
			address += '/' + items
		address += '/' + navigate

		os.chdir(address)
		pythonNavigator()

	else:
		print('Option not available')

pythonNavigator()