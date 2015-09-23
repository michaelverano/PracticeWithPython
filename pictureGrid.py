grid = [
	
	['.', '.', '.', '.', '.', '.'],
	['.', '0', '0', '.', '.', '.'],
	['0', '0', '0', '0', '.', '.'],
	['0', '0', '0', '0', '0', '.'],
	['.', '0', '0', '0', '0', '0'],
	['0', '0', '0', '0', '0', '.'],
	['0', '0', '0', '0', '.', '.'],
	['.', '0', '0', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.']
		] #x_axis goes down, y_axis goes across

y_axis = 0

while y_axis < 6:
	image = ''
	#This shit works going down
	x_axis = 0
	while x_axis < len(grid): 
		image += grid[x_axis][y_axis]	
		x_axis += 1
	y_axis += 1
	print(image)