#! python3
#  PhoneAndEmail.py - finds phone numbers and email addresses on the clipboard.

import pyperclip, re

def findPhoneNumbers(answer):

	text = pyperclip.paste()
	#print(text) #Test
	
	# Filters out for phone numbers.
	phoneRegex = re.compile(r"""(

		(\d{3}|\(d{3}\)) 				# Area Code
		(\s[-]\.)?						# Separator
		(\d{3})							# First 3 digits
		(\s[-]\.)?						# Separator
		(\d{4})							# Last 4 digits
		(\s*(ext|x|ext.)\s*(\d{2,5}))?	# Extension

		)""", re.VERBOSE)

	
	items = phoneRegex.findall(text)
	outPut(items, answer)

def findEmails(answer):
	text = pyperclip.paste()
	#print(text)

	# Filters out for emails.
	emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+				# name on email
		@								# the at symbol
		[a-zA-Z0-9.-]+					# domain name
		.								# dot
		[a-zA-Z]						# something

		)''', re.VERBOSE)

	items = emailRegex.findall(text)
	#print(items)
	outPut(items, answer)

def passwordStrength(answer):
	text = pyperclip.paste()

	passWordRegex = re.compile(r'''(
		([a-zA-Z0-9._%+-]+				# name on email
		@								# the at symbol
		[a-zA-Z0-9.-]+					# domain name
		.								# dot
		[a-zA-Z])						# something
		\n 								# new line
		([a-zA-Z0-9._%+-]+)				# Any text

		)''', re.VERBOSE)	


	items = passWordRegex.findall(text)
	
	for password in items:
		#print(password) #Test to see if I have the right thing copied.
		Capital_Letters = False
		Numbers = False
		print('\n' + password[2])

		# code that can figure out if the text has 8+ characters,
		if len(password[2]) >= 8:
			
			caps = re.search('[A-Z]', password[2]) # Does the password have capital letters?
			if caps != None:
				Capital_Letters = True
				print('Password has capital letters.')	
			else:
				print('Password does not have capital letters.')
			
			nums = re.search(r'\d', password[2]) # does the password have numbers?
			#print(nums) #Test to see if the password has a number or not.
			
			if nums != None:
				Numbers = True
				print('Password has numbers.')
			else:
				print('Password needs numbers.')
			
			if Capital_Letters == True and Numbers == True:
				print('Password Strength is strong')
			else: 
				print('Password strength is weak.')
		else:
			print('Password has less than 8 characters.')
			print('Password is weak.')
			
def outPut(items, answer):
	if items == []:
		print('There are no ' +  answer + 's in your clipboard.')
		exit()

	group = []
	if answer == 'Phone Number':
		for i in items:
			group.append('('+i[1]+')'+i[3]+'-'+i[5])
	if answer == 'Email':
		for i in items:
			group.append(i)
	if answer == 'Password Strength':
		print(items)


	print('\nHere are the ' + answer + 's attached to your clipboard:')
	for i in group:
		print(i)
	

	initiate()

def initiate():
	"""options = {
		'Phone Number'	:	findPhoneNumbers(answer),
		'Email'			:	findEmails(answer),
		'Password'		:	passwordStrength(answer)
		}""" #Future code when I come back to this.

	print('''\nWhat would you like to find? 
		"Phone Number"
		"Email"
		"Password Strength"
		Type "EXIT" to exit program.\n'''
		)

	answer = input('Phone Number or Email? > ')

	if answer == 'Phone Number':
		findPhoneNumbers(answer)
	elif answer == 'Email':
		findEmails(answer)
	elif answer == 'Password Strength':
		passwordStrength(answer)
	elif answer == 'EXIT':
		exit(0)
	else:
		print('Sorry, that is not an option! D:')
		initiate()

if __init__ == '__main__':
	initiate()