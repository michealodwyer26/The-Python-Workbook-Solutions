print("This program calculates the real roots of a quadratic equation(if any).")
a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))

discriminate = b**2 - 4*a*c

if discriminate < 0:
	print("This quadratic function doesn't have any real roots.")
	
elif discriminate == 0:
	print("This quadratic function has one real root.")
	
	root = -b / 2*a 
	
	print("Real root = {}".format(root))
	
elif discriminate > 0:
	print("This quadratic function has two real roots.")
	
	root1 = -b + discriminate / 2*a
	root2 = -b - discriminate / 2*a 
	
	print("Real roots = {} or {}".format(root1, root2))