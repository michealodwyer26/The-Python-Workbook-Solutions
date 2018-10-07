sum = 0
n = 0

interrupted = False
while not interrupted:
	val = int(input("Enter a value (0 to exit): "))
	if val != 0:
		sum += val
		n += 1
	else:
		interrupted = True 
		
avg = sum / n 
print("The average is {}.".format(avg))