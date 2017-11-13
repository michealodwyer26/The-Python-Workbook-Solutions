import math

t1 = float(input("Please enter the x value of a point on Earth in degrees: "))
t2 = float(input("Please enter the y value for that point on Earth in degrees: "))

g1 = float(input("Please enter the x value of a 2nd point on Earth in degrees: "))
g2 = float(input("Please enter the y value for that point on Earth in degrees: "))

distance = 6371.01 * math.acos(math.sin(math.radians(t1)) * math.sin(math.radians(g1)) + \
math.cos(math.radians(t1)) * math.cos(math.radians(g1)) * math.cos(math.radians(t2-g2)))

print("The distance between these two points on Earth is {}km".format(distance))