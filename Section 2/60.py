import random

space = random.randint(0, 37)

if space == 0:
	if random.randint(0, 2) == 0:
		print("Pay 00")
	else:
		print("Pay 0")
		
else:
	print("The spin resulted in {}...".format(space))

	print("Pay {}".format(space))
	
	if space == 1 or space == 3 or space == 5 or space == 7 or space == 9 or space == 12 or space == 14 or space == 16 or space == 18 \
	or space == 19 or space == 21 or space == 23 or space == 25 or space == 27 or space == 30 or space == 32 or space == 34 or space == 36:
		print("Pay Red")
	else:
		print("Pay Black")
		
	if space > 0:
		if space % 2 == 0:
			print("Pay Even")
		else:
			print("Pay Odd")
	
	if space >= 1 and space <= 18:
		print("Pay 1 to 18")
	elif space >= 19 and space < 36:
		print("Pay 19 to 36")
		