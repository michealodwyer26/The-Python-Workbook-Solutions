noOfSides = int(input("Please enter the number of sides of a shape: "))

if noOfSides == 3:
	print("That is a triangle.")
elif noOfSides == 4:
	print("That is a square.")
elif noOfSides == 5:
	print("That is a pentagon.")
elif noOfSides == 6:
	print("That is a hexagon.")
elif noOfSides == 7:
	print("The is a heptagon.")
elif noOfSides == 8:
	print("That is an octagon.")
elif noOfSides == 9:
	print("That is a nonagon.")
elif noOfSides == 10:
	print("That is a decagon")
else:
	print("Please enter an integer greater than 2")