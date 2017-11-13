import math

height = float(input("Please enter a height from which an object is dropped from in meters: "))

acceleration = 9.8
finalVelocity = math.sqrt(2*acceleration*height)

print("The final velocity when the object hits the ground is {}m/s^2.".format(finalVelocity))