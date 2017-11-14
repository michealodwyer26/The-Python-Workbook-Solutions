bankNoteAmount = int(input("Please enter a bank note amount: $"))

individualName = ""

if bankNoteAmount == 1:
	individualName = "George Washington"
if bankNoteAmount == 2:
	individualName = "Thomas Jefferson"
if bankNoteAmount == 5:
	individualName = "Abraham Lincoln"
if bankNoteAmount == 10:
	individualName = "Alexander Hamilton"
if bankNoteAmount == 20:
	individualName = "Andrew Jackson"
if bankNoteAmount == 50:
	individualName = "Ulysses S. Grant"
if bankNoteAmount == 100:
	individualName = "Benjamin Franklin"
	
if individualName == "":
	print("That is not an American bank note in circulation.")
else:
	print("The individual on this bank note is {}.".format(individualName))