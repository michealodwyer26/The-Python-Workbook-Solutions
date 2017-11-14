dbLevel = float(input("Please enter a dB level: "))

if dbLevel < 40:
	print("This is extremely quite.")
elif dbLevel > 130:
	print("This is extremely loud.")
	
	
if dbLevel > 40:
	print("This is between a quiet room and an alram clock.")
elif dbLevel > 70:
	print("This is between an alarm clock and a gas lawnmower.")
elif dbLevel > 106:
	print("This is between a gas lawnmower and a jackhammer.")
	
if dbLevel == 40:
	print("This is a quiet room.")
elif dbLevel == 70:
	print("This is an alarm clock.")
elif dbLevel == 106:
	print("This is a gas lawnmower.")
elif dbLevel == 130:
	print("This is a jackhammer.")