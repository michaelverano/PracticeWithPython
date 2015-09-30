#!	python3

import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  # turns debug mode off.

guess = ''

while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()

logging.debug('Guess is ' + str(guess))
toss = random.randint(0, 1) # 0 is tails, 1 is heads.

if toss == 1:
	toss = 'heads'
elif toss == 0:
	toss = 'tails'
else:
	print('That isn\'t an option!')

logging.debug('Testing toss conversion - toss = ' + str(toss) )



if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	if toss	== guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')