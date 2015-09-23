#! python3 
# csvTest.py - Just a test to see if I can do CSV stuff before I actually learn it.

import csv

# taken from the documentation.
with open('drugs-and-math.csv', newline ='') as csvfile:
	fileReader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
	for row in fileReader:
		print(', '.join(row))