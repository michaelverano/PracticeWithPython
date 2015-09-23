inventory = {
	'rope': 1,
	'torch': 6,
	'gold coin': 42,
	'dagger': 1,
	'arrow': 12
	}

def displayInventory(stuff):
	amount = 0
	for v, k in stuff.items():
		print(str(k) + ' ' + str(v))
		amount = amount + k
	print('Total number of items: ' + str(amount))

displayInventory(inventory)