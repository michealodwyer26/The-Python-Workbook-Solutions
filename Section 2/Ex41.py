noteAndOctave = input("Please enter a musical note: ")

# Notes are written in the form note, octave eg. C4
note = noteAndOctave[0].upper()
octave = int(noteAndOctave[1])

frequency = -1

if note == "C":
	frequency = 261.63
elif note == "D":
	frequency = 293.66
elif note == "E":
	frequency = 329.63
elif note == "F":
	frequency = 349.23
elif note == "G":
	frequency = 392.00
elif note == "A":
	frequency = 440.00
elif note == "B":
	frequency = 493.88
	
frequency /= 2 ** (4 - octave) # Formula to find the frequency in a different octave
	
print("The note's frequency is {}Hz".format(frequency))