month = input("Please enter the name of a month: ").lower()
day = int(input("Please enter a day from that month: "))

season = ""

spring, summer, fall, winter = False

if month == "march" or month == "april" or month == "may" or month == "june":
	if month == "march" and day >= 20:
		spring = True
		
	elif month == "april" or month == "may":
		spring  = True
		
	elif month == "june" and day < 21:
		spring = True
		
if month == "june" or month == "july" or month == "august" or month == "septemper":
	if month  == "june" and day >= 21:
		summer = True
		
	elif month == "july" or month == "august":
		summer = True
		
	elif month == "semptember" and day < 22:
		summber = True
		

if month == "septemper" or month == "october" or month == "november" or month == "december":
	if month == "september" and day >= 22:
		fall = True
		
	elif month == "october" or month == "november":
		fall = True
		
	elif month == "december" and day < 21:
		fall = True
		
if month == "december" or month == "january" or month == "february" or month == "march":
	if month == "december" and day >= 20:
		winter = True
		
	elif month == "january" or month == "february":
		winter = True
		
	elif month == "march" and day < 20:
		winter = True
		
if spring:
	print("That date falls in spring.")
elif summer:
	print("That date falls in summer.")
elif fall:
	print("That date falls in fall.")
elif winter:
	print("That date falls in winter.")