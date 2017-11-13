import math

s = float(input("Please enter the size of a side of a regular polygon: "))
n = float(input("Please enter the number of these sides in the regular polygon: "))

area = (n * (s*s)) / (4 * math.tan(math.pi/n))

print("The area of this polygon is {} units squared.".format(area))