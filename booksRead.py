#! 	python3
#	booksRead.py - just a database using Shelve to keep track of the books
#			I've read.
#	FUTURE TO DO: TURN THIS INTO A GUI


import shelve, re, os

#bookshelf = shelve.open('redpillbooks')
#bookshelf.close()

# Goes into the eBooks folder and saves the books I currently have.
def bookFinder():
	os.chdir('/home/michael/Ubuntu Stuff/eBooks')
	

	booksList = []
	for items in os.listdir():
		booksList.append(items)

	readOrNot(booksList)

def readOrNot(bookList): # Cycles through the list in booksList to see if I read the book or not.
	read = []
	not_read = []
	no_answer = []

	counter = 0
	for items in bookList:
		if os.path.isfile(items):
			print('\n\n\n\nDid you read this book?  : ' + items + '\n(next: ' + bookList[counter+1] + ')')
			answer = input('> ')

			if answer.lower() == 'yes':
				read.append(items)
			elif answer.lower() == 'no':
				not_read.append(items)
			else:
				print('That\'s not one of the answers.')
				no_answer.append(items)
		counter += 1
	print('Books to read: ' + str(not_read))
	print('Books I\'ve read: ' + str(read))

# Take the redpillbooks.txt file and filter out and seperate them into different
# levels.
def bookFilter():
	redpillbooks = open('redPillbooks.txt')
	
	readBooks =	redpillbooks.read()
	print(readBooks)




	redpillbooks.close()

bookFinder()
