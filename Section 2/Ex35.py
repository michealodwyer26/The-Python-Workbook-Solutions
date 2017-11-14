humanYearsOld = int(input("Please enter the age of a dog in human years: "))

humanYearsOld = 0
	
if humanYearsOld <= 2:
	dogYears = humanYearsOld * 10.5
elif humanYearsOld > 2:
	dogYears = 2 * 10.5
	dogYears += (humanYearsOld-2) * 4

if humanYearsOld == 0:
	print("Please enter a positive integer.")
else:
	print("The dog is {} years old in dog years.".format(dogYears))