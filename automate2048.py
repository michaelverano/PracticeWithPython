#!	python3
#	automate2048.py - Automates the 2048 game for you using Selenium and a loop statement.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging 
import sys
import random

# Debug mode on for testing
def debugMode(mode):
	logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
	
	if mode == 'Off':
		logging.disable(logging.CRITICAL) # This turns off debug mode.
		print('Debug mode off...')
	logging.debug('Program on...')
	logging.debug('Debug mode on...')

def navigateToGame():
	logging.debug('Opening browser...')
	browser = webdriver.Firefox()
	logging.debug('Going to 2048 game...')
	browser.get('https://gabrielecirulli.github.io/2048/')
	return browser

def automate248(mode):
	logging.debug('Automating 2048...')
	browser.implicitly_wait(5)
	htmlElem = browser.find_element_by_css_selector('.game-container')

	scoreElem = browser.find_element_by_css_selector('.score-container')

	while True:
		browser.implicitly_wait(3)
		randomMovement = random.randint(0,3) 
		logging.debug('Number is...' + str(randomMovement))
		browser.implicitly_wait(2)

		# 1 = up, 2 = down, 3 = left, 4 = right
		if randomMovement == 0:
			logging.debug('Up')
			htmlElem.send_keys(Keys.UP)
		elif randomMovement == 1:
			logging.debug('Down')
			htmlElem.send_keys(Keys.DOWN)
		if randomMovement == 2:
			logging.debug('Left')
			htmlElem.send_keys(Keys.LEFT)
		elif randomMovement == 3:
			logging.debug('Right')
			htmlElem.send_keys(Keys.RIGHT)

		

		browser.implicitly_wait(3) # wait 2 seconds


if __name__ == '__main__':
	# Debug mode.
	if len(sys.argv) == 1:
		mode = 'Off'
	elif len(sys.argv) > 1 and sys.argv[1] == 'debug':
		mode = 'On'
	

	debugMode(mode)
	browser = navigateToGame()
	automate248(mode)