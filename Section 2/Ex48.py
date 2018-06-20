year = int(input("Please enter any year after A.D.: "))

if year < 2000 or year > 2011:
	while year < 2000:
		year += 12 
	while year > 2011:
		year -= 12

if year == 2000:
	sign = "Dragon"
elif year == 2001:
	sign = "Snake"
elif year == 2002:
	sign = "Horse"
elif year == 2003:
	sign = "Sheep"
elif year == 2004:
	sign = "Monkey"
elif year == 2005:
	sign = "Rooster"
elif year == 2006:
	sign = "Dog"
elif year == 2007:
	sign = "Pig"
elif year == 2008:
	sign = "Rat"
elif year == 2009:
	sign = "Ox"
elif year == 2010:
	sign = "Tiger"
elif year == 2011:
	sign = "Hare"
	
print("You are nothing but a {}!".format(sign))
print("(according to Chinese Zodiac signs, of course...)")