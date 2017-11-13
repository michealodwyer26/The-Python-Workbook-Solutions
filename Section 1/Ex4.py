width = int(input("Please enter the width of the field in feet: "))
length = int(input("Please enter the length of the field in feet: "))

sqFeetPerAcre = 43560

area = (width * length) / sqFeetPerAcre

print("The area of the field in acres is {} acres.".format(area))