#! 	Python3
#	directoryExplorer.py - Navigates the directory.
#	I wrote this so I don't have to keep writing this on programs working
#	with the operating system.

# 	Doesn't work as intented when imported into another program. Fix dis.
import os

def directoryExplorer(current_directory):
	
	move_backwards = current_directory.split(os.sep)
	move_forwards = next(os.walk(current_directory))[1] # Learn how this works

	print('\nThis is your current directory: ' + current_directory)
	print('These are the folders available in your current directory: ' + str(os.path.basename(current_directory)))
	print(move_forwards)
	print('where do you want to go?\n')
	
	go_to = input(""" Options...
		1. Pick a directory to move forward.
		2. Type BACK to move back a directory.
		3. Type STAY to stay in directory,
		4. Type EXIT to escape program.\n > """)

	if go_to.lower() == 'back': #Move Back
		print('Moving backwards to ' + os.path.split(os.getcwd())[0])
		new_path = os.path.split(os.getcwd())[0] 
		os.chdir(new_path)
		directoryExplorer()
	elif go_to in move_forwards: # Move Forwards
		print('moving forwards to ' + str(go_to))
		new_path = os.getcwd() + '/'+ go_to
		os.chdir(new_path)
		directoryExplorer()
	elif go_to.lower() == 'stay': # Stay
		print('Staying in this directory.')
	elif go_to.lower() == 'exit':
		exit()
	else: # Exit program
		print('That is not an option')
		directoryExplorer()



if __name__ == '__main__':
	current_directory = os.getcwd()
	directoryExplorer(directory)