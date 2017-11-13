import math

s1 = float(input("Please enter side a of a triangle: "))
s2 = float(input("Please enter side b of a triangle: "))
s3= float(input("Please enter side c of a triangle: "))

s = (s1+s2+s3) / 2

area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))

print("The area of the triangle is {} units squared.".format(area))