#! 	python3
#	randomSentences.py - generates a random sentences from a list of nounds, verbs
#						adverbs, and adjectives and generates a bunch of sentences 
#						on one file.

import os, random, re
import time

# TODO: Import the list from files that contain the list of nouns, verbs, adverbs, 
#				and adjectives.
def random_words(words):
	words = open(words + '.txt')
	read_words = words.read() # all the characterse in the file are in one big string.
	
	words = read_words.split() # take the string and break parts of it into words.

	random_number = random.randint(0, len(words) - 1)

	return(words[random_number])

# TODO: create template sentence
# FUTURE ADVANCED TODO: Create a file where you can create the sentences.
template_sentence = """

		In order to <VERB> your <NOUN> <ADVERB>, 
		you must <VERB> your <NOUN> in <ADJECTIVE> <NOUN>. 
		Then, <VERB> it across your <NOUN> 5000 times. 
		This will <VERB> off any remainig <NOUN>.
		When you are <VERB> you should <VERB> the <NOUN> in <ADJECTIVE> <NOUN> to <VERB> it. 
		You should also <VERB> your <NOUN> with a <ADJECTIVE> <NOUN> to keep it <ADJECTIVE> and <ADJECTIVE>.
		This will keep also keep away <NOUN>. Don`t worry.
		It is normal to experience <NOUN> the first time you try this.
		Consult your <NOUN> if you break out in <NOUN>.
		This works well on your <NOUN> too!

				"""

#This needs work. Do I got the list route or the regex route?
def madLibs(madlib_template):
	split_words = template_sentence.split()
	# print(template_sentence)
	
	nounRegex = re.compile(r'<NOUN>[.,?!]|<NOUN>')
	verbRegex = re.compile(r'<VERB>[.,?!]|<VERB>')
	adverbRegex = re.compile(r'<ADVERB>[.,?!]|<ADVERB>')
	adjectiveRegex = re.compile(r'<ADJECTIVE>[.,?!]|<ADJECTIVE>')

	#print(split_words)
	counter = 0
	
	for items in split_words:
		
		if nounRegex.match(items):
			split_words[counter] = random_words('nouns')
		elif verbRegex.match(items):
			split_words[counter] = random_words('verbs')
		elif adverbRegex.match(items):
			split_words[counter] = random_words('adverbs')
		elif adjectiveRegex.match(items):
			split_words[counter] = random_words('adjectives')
		
		counter += 1 

	new_sentence = ''
	for items in split_words:
		new_sentence += ' ' + items	

		if float(counter % 4) == 0:
			new_sentence += '\n'

		counter += 1

	createFile(new_sentence)

# Function that creates a new folder for the file and then appends the file.
def createFile(sentence):
	hour = time.strftime('%I')
	minutes = time.strftime('%M')
	seconds = time.strftime('%S')
	Day = time.strftime('%d')
	Month = time.strftime('%b')
	Year = time.strftime('%Y')
	Day_Name = time.strftime('%a')

	if os.path.exists('./madLibs'):
		os.chdir('./madLibs')
		madLibs = open('madLibs.txt', 'a')
		madLibs.write('\n' + ' written on: ' + str(Day) + ' ' + str(Month) + ' ' + str(Year) + ' at ' + str(hour) + ':'+ str(minutes) + '.'+ str(seconds) + '\n')
		madLibs.write(sentence)
		madLibs.write('\n')
		madLibs.close()
		print('Our madlibs files have been added, yo! Check it outself.')
	else:
		os.mkdir('./madLibs')
		createFile(sentence)

madLibs(template_sentence)
