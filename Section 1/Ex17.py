mass = float(input("Please enter the mass of some water in grams: "))
tempChange = float(input("Please enter the temperature changein degrees Celsius: "))

C = 4.186 # Water's heat capacity is 4.186 Joules
joules = mass * C * tempChange

print("Total amount of energy used in Joules is {}.".format(joules))

costPerKiloWattHour = 8.9 # Taken from the question
kiloWattHours = joules * 2.7778e-7 # Converts from Joules to kilowatt-hours

cost = kiloWattHours * costPerKiloWattHour

print("The total cost of this is ${}.".format(cost))

