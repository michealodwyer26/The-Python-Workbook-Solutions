year =  int(input("Enter a year: "))

is_leap_year = False

if year % 400 == 0:
	is_leap_year = True
elif year % 100 == 0 and not year % 400 == 0:
	is_leap_year = False 
elif year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
	is_leap_year = True 

if is_leap_year:
	print("That year is a leap year.")
else:
	print("That year is not a leap year.")