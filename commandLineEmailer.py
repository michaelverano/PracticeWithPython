#!	python3
#	commandLineEmailer.py - takes two strings from the command line, an email to send to and the message,
#	Then goes onto Firefox, goes to Google, logs onto gmail account, then types the message and sends it.

# 	To do list to improve the program: Make something on the subject page...

from selenium import webdriver
import sys 
import logging
import getpass

def debugMode(On):

	if On == False:
		logging.disable(logging.CRITICAL)
	
	# Debug mode On.
	logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
	logging.debug('Program starting...')

	# Test what's being passed on the arguments.
	logging.debug('First command line argument passed is: ' + str(sys.argv[0]))
	logging.debug('Second command line argument passed is: ' + str(sys.argv[1]))
	logging.debug('Third command line argument passed is: ' + str(sys.argv[2]))
	logging.debug('This is a list of what is passed on to the system: ' + str(sys.argv))

def makeMessage(arguments, debugOffMode):
	# print the message
	emailMessage = ''
	for words in sys.argv[debugOffMode + 2:]:
		emailMessage += ' ' + words

	logging.debug('This is the email message: ' + emailMessage)
	
	#print(emailMessage) # used for testing the debugger.
	return emailMessage

def runBrowserToGmail():
	# This method works for gmail account.
	browser = webdriver.Firefox()
	browser.get('http://gmail.com')
	
	# Log into gmail account.
	username = input('What is your gmail username: ')
	emailElem = browser.find_element_by_id('Email')
	logging.debug('Email element found...')
	emailElem.send_keys(username)
	logging.debug('username sent to the text field....')
	nextElem = browser.find_element_by_id('next')
	logging.debug('"next" element found...')
	nextElem.submit()
	logging.debug('Email account sent to gmail...')


	# put in email password.
	logging.debug('Waiting 3 seconds...')
	browser.implicitly_wait(3) # Wait for the page to load entirely.
	passwd = getpass.getpass('What is your password: ')

	passwordElem = browser.find_element_by_id('Passwd') 
	logging.debug('Password element found...')
	passwordElem.send_keys(passwd)
	logging.debug('Password in text field...')
	passwordElem.submit()
	logging.debug('Password sent to gmail...')

	return browser


# TODO: Make this function.
def writeEmail(message, email, browser):
	# Click on the compose button.
	compElem = browser.find_element_by_css_selector('.T-I-KE')
	compElem.click()
	logging.debug('Compose button is clicked...')

	# wait x seconds.
	logging.debug('Waiting 4 seconds...')
	browser.implicitly_wait(4)
	
	# click on the send-to form and input the email to send. 
	messElem = browser.find_element_by_tag_name('textarea')
	logging.debug('send-to fill area clicked...')
	messElem.send_keys(email)
	logging.debug('email typed into field...')

	# click on the subject.
	subElem = browser.find_element_by_css_selector('.aoT')
	subElem.send_keys('This is a test message using the Selenium program...')

	# click on the message area and input the message.
	textElem = browser.find_element_by_css_selector('.Al')
	textElem.send_keys(message)

	# find the send button.
	sendElem = browser.find_element_by_css_selector('.aoO')
	# In the future, figure out a way to turn this off when debug mode is on.
	#sendElem.click()
	logging.debug('Message sent...')


if __name__ == '__main__':
	# Debug mode can now be turned on or off by typing 'debugOff' on sys.argv[1]
	debugOffMode = 0
	if sys.argv[1] == 'debug_off':
		debugMode(False)
		debugOffMode = 1
	else:
		debugMode(True)

	# Makes a message from the input from sys.arv[2:]
	message = makeMessage(sys.argv, debugOffMode)
	logging.debug('emailMessage off of function is: ' + str(makeMessage))
	
	# Run the browser to go to log on to gmail.
	browser = runBrowserToGmail()
	
	# Once logged on, write the message and send it.
	writeEmail(message, sys.argv[1], browser)
