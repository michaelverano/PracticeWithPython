import copy 

hotdog = [['A', 'B', 'C,'], ['D', 'E', 'F', ['G', 'H', 'I']]]

print('\n using copy.copy() with lists in a list')
pancake = copy.copy(hotdog)
#pancake[0] = 35
print(hotdog)
print(pancake)
print('')


print('\n using copy.deepcopy() with lists in a list')
juice = copy.deepcopy(hotdog)
#juice[0] = 33
print(hotdog)
print(juice)
print('')
