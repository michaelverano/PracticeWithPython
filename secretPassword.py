passwordFile = open('SecretPasswordFile.txt')
secretPassword = str(passwordFile.read())
print('Enter your password.')
typedPassword = str(input())

if typedPassword == secretPassword:
	print('Access Granted')
	if typedPassword == '12345':
		print('That password is one that an idiot puts on their luggage.')
else:
	print('Access Denied')
