import string, random

def passgenerator (amount):
	while (amount > 0):
		print(''.join(random.sample(random.sample(string.digits, 10)+random.sample(string.lowercase, 10)+random.sample(string.uppercase, 10), 10)))
		amount = amount - 1


passgenerator(5)