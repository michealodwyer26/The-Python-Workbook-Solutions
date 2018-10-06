licensePlate = input("Enter a license plate: ")

styleOfPlate = ""

if licensePlate[0] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and licensePlate[1] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and licensePlate[2] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
	if licensePlate[3] in "0123456789" and licensePlate[4] in "0123456789" and licensePlate[5] in "0123456789":
		styleOfPlate = "old"

elif licensePlate[0] in "0123456789" and licensePlate[1] in "0123456789" and licensePlate[2] in "0123456789" and licensePlate[3] in "0123456789":
	if licensePlate[4] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and licensePlate[5] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and licensePlate[6] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
		styleOfPlate = "new"
		
if styleOfPlate == "old":
	print("This is an old style plate.")
elif styleOfPlate == "new":
	print("This is a new style plate.")
else:
	print("Invalid license plate entered.")
		