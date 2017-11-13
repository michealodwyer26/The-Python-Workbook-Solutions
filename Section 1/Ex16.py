import math

r = float(input("Please enter a radius r: "))

area = math.pi * (r * r)
vol = (4/3) * math.pi * (r * r * r)

print("The area of a circle with radius r is {} units squared.".format(area))
print("The volume of a sphere with radius r is {} units cubed.".format(vol))