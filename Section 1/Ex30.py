kiloPascals = float(input("Please enter a pressure in kilo-pascals: "))

PSI = kiloPascals * 0.145037738
mmOfMercury = kiloPascals * 7.50062
atmospheres = kiloPascals / 101.3

print()
print("In Pounds Per Square Inch (PSI): {}".format(PSI))
print("In Millimetres Of Mercury (mmHg): {}".format(mmOfMercury))
print("In Atmospheres (atm): {}".format(atmospheres))