if symbol_database = {
	'?' 		: 'Matches zero or one of the preceding group.',
	'*' 		: 'matches zero or more of the preceding group.',
	'+' 		: 'matches one or more of the preceding group.',
	'{n}' 		: 'matches exactly n of the preceding group.',
	'{n,}' 		: 'matches n or more of the preceding group.',
	'{,m}' 		: 'matches 0 to m of the preceding group.',
	'{n,m}' 	: 'matches at least n and at most m of the preceding group.',
	'^spam' 	: 'means the string must begin with spam.',
	'spam$' 	: 'means the string must end with spam.',
	'.' 		: 'matches any character, except newline characters.',
	r'\d' 		: 'match a digit.',
	r'\w'		: 'match a word.',
	r'\s'		: 'match a space character.',
	r'\D'		: 'match anything except a digit.',
	r'\W'		: 'match anything except a word.',
	r'\S' 		: 'match anything except a space character.',
	'[abc]'		: 'matches any character between the brackets (such as a, b, or c)',
	r'[^abc]'	: 'matches any character that isn\'t between the brackets.'
	}


def regexSymbolDictionary(database):
	print(
		r'''
		What regex symbol do you want to know?

		? * + {n} {n,} {,m} {n,m,} {n, m}? *? +? ^spam spam$ 

		. \d \w \s

		\D \W \S 

		[abc] [^abc]
		
		Press [ENTER] with no text to exit.

		'''
		)

	request = input('> ')
	
	print(request)


	while request != '':

		if request in database.keys():
			print(database[request])
		else:
			print('What you\'re looking for isn\'t in the database!')
	
		request = input('\nWhat regex symbol do you want to know? \n> ')



regexSymbolDictionary(symbol_database)