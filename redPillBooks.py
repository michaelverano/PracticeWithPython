#! 	python3
#	redPillBooks.py - just a database using Shelve to store the books from the Red Pill.

import shelve, re

rpbookshelf = shelve.open('redpillbooks')

# Take the redpillbooks.txt file and filter out and seperate them into different
# levels.
def bookFilter():
	redpillbooks = open('redPillbooks.txt')
	
	readBooks =	redpillbooks.read()
	print(readBooks)


	redpillbooks.close()

rpbookshelf.close()