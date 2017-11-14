month = input("Please enter the name of a month: ").lower()

if month == "september" or month == "april" or month == "june" or month == "november":
	print("There are 30 days in this month.")
elif month == "february":
	print("There are 28 or 29 days in this month.")
else:
	print("There are 31 days in this month.")