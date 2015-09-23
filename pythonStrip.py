#! Python3
# pythonStrip.py A function that works the same way as strip().

import re

"""
Works the same way as strip().
pythonStrip([arg1], [arg2])
First parameter is the string to strip the whitespace characters in the beginning and end.
Characters passed to the second argument of the function will be removed from the string.
"""

test_string1 = '             test string 1 2 3 4                 '
test_string2 = 	"""
					\ttest string

				"""
def pythonStrip(passed_string, character_to_remove):

	# Regex made to remove white spaces.
	whiteSpaceRegex = re.compile(r'(\b.*\b)')

	test = whiteSpaceRegex.findall(passed_string)
	
	# Does the character_to_remove function have something in it?
	if character_to_remove == '':
		print(test[0])
		#print('There is no character.')
	else:
		#print('You have soemthing on "character to remove"')
		split_string = passed_string.split()

		if character_to_remove in split_string:
			split_string.remove(character_to_remove)
			
		print(split_string)

# Introduction
print(	'''	What would you like to test?
			test_string1
			test_string2
			test_string3

			'exit' to exit
		''')

# While loop to keep the program running until told to stop.
string = ''
while string != 'exit':
	string = input('> ')

	if string == 'test_string1':
		print('Is there a character that you\'d like to remove?')
		character_to_remove = input('Leave empty if you don\'t have a string to remove: ')
		pythonStrip(test_string1, character_to_remove)
	elif string == 'test_string2':
		print('Is there a character that you\'d like to remove?')
		character_to_remove = input('Leave empty if you don\'t have a string to remove:	')
		pythonStrip(test_string2, character_to_remove)
	elif string == 'test_string3':
		print('Not yet ready.')
	elif string == 'exit':
		exit()
	else:
		print('That\'s not an option.')
else:
	exit()