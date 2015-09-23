dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
current_inventory = {
	'gold coin': 42,
	'rope': 1
	}

# Adds to yo shit
def addToInventory(inventory, addedItems):
	#Add yo shit
	for things in addedItems:
		if things in current_inventory.keys():
			#print('True') # Test to see if item is there
			current_inventory[things] += 1
		else:
			#print('False') # Test to see if item is there
			current_inventory[things] = 1

	#Count yo shit
	stuff = 0
	for a, b in inventory.items():
		stuff += b
	
	#Print yo shit
	print('Inventory: ')
	for a, b in inventory.items():
		print(str(b) + ' ' + str(a))

	#Print total number of shit
	print('Total number of items: ' + str(stuff))

addToInventory(current_inventory, dragonLoot)