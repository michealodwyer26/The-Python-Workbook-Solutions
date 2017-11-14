gridPos = input("Please enter a chess board position: ")

col = gridPos[0].lower()
row = int(gridPos[1])

if col in "aceg":
	colStartsWithBlack = True
else:
	colStartsWithBlack = False
	
	
if colStartsWithBlack:
	if row % 2 == 0:
		white = True
	else:
		white = False
else:
	if row % 2 == 0:
		white = False
	else:
		white = True
		
if white:
	print("That position is coloured white.")
else:
	print("That position is coloured black.")