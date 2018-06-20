month = int(input("Please enter your month of birth as a number: "))
date = int(input("Please enter your day of birth as a number: "))

assert month <= 12 and month >= 1
assert date <= 31 and month >= 1


zodiac = ""

if (month == 12 and date >= 22) or (month == 1 and date <= 19):
	zodiac = "Capricorn"
	
elif (month == 1 and date >= 20) or (month == 2 and date <= 18):
	zodiac = "Aquarius"
	
elif (month == 2 and date >= 19) or (month == 3 and date <= 20):
	zodiac = "Pisces"
	
elif (month == 3 and date >= 21) or (month == 4 and date <= 19):
	zodiac = "Aries"
	
elif (month == 4 and date >= 20) or (month == 5 and date <= 20):
	zodiac = "Taurus"

elif (month == 5 and date >= 21) or (month == 6 and date <= 20):
	zodiac = "Gemini"
	
elif (month == 6 and date >= 21) or (month == 7 and date <= 22):
	zodiac = "Cancer"
	
elif (month == 7 and date <= 23) or (month == 8 and date <= 22):
	zodiac = "Leo"
	
elif (month == 8 and date >= 23) or (month == 9 and date <= 22):
	zodiac = "Virgo"
	
elif (month == 9 and date >= 23) or (month == 10 and date <= 22):
	zodiac = "Libra"
	
elif (month == 10 and date <= 23) or (month == 11 and date <= 21):
	zodiac = "Scorpio"
	
elif (month == 11 and date <= 22) or (month == 12 and date <= 21):
	zodiac = "Sagittarius"
	
print("You are a thrifty {}!".format(zodiac))
	