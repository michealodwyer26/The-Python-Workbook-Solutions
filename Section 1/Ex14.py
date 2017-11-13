feet = int(input("How many feet: "))
inches = int(input("How many inches: "))

inches += feet * 12

metres = inches * 2.54

print("This height is {}m.".format(metres))