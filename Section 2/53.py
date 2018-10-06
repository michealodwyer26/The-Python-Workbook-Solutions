value = float(input("Enter a value for the employee's performance: "))

descriptor = ""

if value == 0.0:
	descriptor = "Unacceptable performance"
elif value == 0.4:
	descriptor = "Acceptable performance"
elif value >= 0.6:
	descriptor = "Meritorious performance"

if descriptor != "":
	print("According to this scale, the employee has shown '{}'.".format(descriptor))
else:
	print("Invalid value entered. (Value is either 0.0, 0.4, or greater than 0.6)")