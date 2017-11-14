s1 = float(input("Please enter the length of first side of a triangle: "))
s2 = float(input("Please enter the length of the second side of the triangle: "))
s3 = float(input("Please enter the length of the third side of the triangle: "))

triangleType = ""

if s1 == s2 == s3:
	triangleType = "equalateral"
elif s1 == s2 or s1 == s3 or s2 == s3:
	triangleType = "isoseles"
else:
	triangleType = "scalene"
	
print("That is a {} triangle.".format(triangleType))
