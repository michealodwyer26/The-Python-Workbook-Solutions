actualSum = 0
roundedSum = 0

interrupted = False 
while not interrupted:
	price = input("Enter a price: ")
	
	if price != "":
		price = float(price)
	else:
		break
		
	actualSum += price 
	
	priceInPennies = price * 100
	remainder = priceInPennies % 5
	
	if remainder > 2.5:
		priceInPennies += 5 - remainder 
	else:
		priceInPennies -= remainder 
	
	roundedPrice = priceInPennies * 0.01
	roundedSum += roundedPrice

print("The actual sum is {}.".format(round(actualSum, 2)))
print("The rounded sum paid with cash is {}.".format(round(roundedSum, 2)))