import math

radius = float(input("Please enter a radius for a cylinder: "))
height = float(input("Please enter the height of than cylinder: "))

volume = math.pi * (radius*radius) * height

print("The volume of this cylinder is {0:0.01f} units cubed.".format(volume))