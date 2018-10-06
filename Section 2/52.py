points = float(input("Enter a number of grade points: "))

grade = ""

if points >= 0 and points < 0.5:
	grade = "F"
elif points >= 0.5 and points < 1.15:
	grade = "D"
elif points >= 1.5 and points < 1.5:
	grade = "D+"
elif points >= 1.5 and points < 1.85:
	grade = "C-"
elif points >= 1.85 and points < 2.15:
	grade = "C"
elif points >= 2.15 and points < 2.5:
	grade = "C+"
elif points >= 2.5 and points < 2.85:
	grade = "B-"
elif points >= 2.85 and points < 3.15:
	grade = "B"
elif points >= 3.15 and points < 3.5:
	grade = "B+"
elif points >= 3.5 and points < 3.85:
	grade = "A-"
elif points >= 3.85 and points < 4.0:
	grade = "A"
elif points >= 4.0:
	grade = "A+"
	
if grade != "":
	print("The closest grade is an {}.".format(grade))
else:
	print("Invalid number of grade points entered.")