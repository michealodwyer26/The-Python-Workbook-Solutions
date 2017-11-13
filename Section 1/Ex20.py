P = float(input("Please enter a pressure in Pascals: "))
V = float(input("Please enter a volume in liters: "))
T = float(input("Please enter a temperature in Kelvin: "))

R = 8.314

n = (P*V) / (R*T)

print("The amount of gas in moles for these conditions is {}.".format(n))