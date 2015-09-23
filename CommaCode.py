print('Feed this monster words! Type STOP to stop feeding it.')

def machine():
	stomach = []
	#stomach = ['A','B', 'C']
	poop = ''
	
	words = input('> ')
	while words != 'STOP':
		stomach.append(words)
		print('moar')
		words = input('> ')
		
	for words in stomach:
		if words == stomach[-1]:
			poop += 'and'
			poop += ' ' + words
			break
		poop += words + ", "
	
	print("\n'You fed this monster " + poop + "'")

machine()