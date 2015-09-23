#! python3.2

tableData = [
	['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose'],
	]

def printTable(tableData):
	colWidths = [0] * len(tableData) # creates a list of the widths for the inner lists in the table

	# Find the longest string in the inner lists.
	counter = 0
	while counter < len(tableData): #loop through the lists of tableData
		
		biggest_number = 0
		for items in tableData[counter]: # find the biggest number per inner list
			
			item_size = len(items)
			if item_size > biggest_number:
				biggest_number = item_size

		# Store largest number in colWidths
		colWidths[counter] = biggest_number 

		counter += 1

	
	# Print the items in a table as per instruction
	# This part doesn't work, yet
	counter = 0
	while counter < len(tableData[0]):
		print(
			tableData[0][counter].rjust(colWidths[0]) + ' ' + 
			tableData[1][counter].rjust(colWidths[1]) + ' ' +
			tableData[2][counter].rjust(colWidths[2])
			)

		counter += 1
		
printTable(tableData)	