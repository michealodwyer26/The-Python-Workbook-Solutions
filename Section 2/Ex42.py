frequency = float(input("Please enter a frequency in Hertz: "))

note = ""

if frequency > 261.63 - 1 and frequency < 261.63 + 1:
	note = "C"
elif frequency > 293.66 - 1 and frequency < 293.66 + 1:
	note = "D"
elif frequency > 329.63 - 1 and frequency < 329.63 + 1:
	note = "E"
elif frequency > 349.23 - 1 and frequency < 349.23 + 1:
	note = "F"
elif frequency > 392.00 - 1 and frequency < 392.00 + 1:
	note = "G"
elif frequency > 440.00 - 1 and frequency < 440.00 + 1:
	note = "A"
elif frequency > 493.88 - 1 and frequency < 493.88 + 1:
	note = "B"
	
if note == "":
	print("This is not an in tune note.")
else:
	print("This is a {} note.".format(note))