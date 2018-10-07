perimeter = 0

x1 = int(input("Enter the x part of the coordinate: "))
y1 = int(input("Enter the y part of the coordinate: "))

interrupted = False 
while not interrupted:
	print()
	x2 = input("Enter the x part of the coordinate (blank to quit): ")
	y2 = input("Enter the y part of the coordinate (blank to quit): ")
	
	if x2 != "":
		x2 = int(x2)
	else:
		break 
	
	if y2 != "":
		y2 = int(y2)
	else:
		break
	
	distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 
	perimeter += distance 
	
	x1 = x2 
	y1 = y2 
	
print()
print("The perimeter of this polygon is {}.".format(perimeter))