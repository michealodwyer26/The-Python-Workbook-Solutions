month = int(input("Please enter in a month with a numerical value (1-12): "))
date = int(input("Please enter in a date: "))

holiday = ""

if month == 1 or month == 4 or month == 12:
	if month == 1 and date == 1:
		holiday = "New Year's Day"
	elif month == 4 and date == 1:
		holiday = "Canada Day"
	elif month == 12 and date == 25:
		holiday = "Christmas Day"
		
if holiday == "":
	print("That is not a holiday that falls on the same date each year.")
else:
	print("That date is {}.".format(holiday))