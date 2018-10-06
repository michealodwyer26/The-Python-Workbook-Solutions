wavelength = int(input("Enter a value for a wavelength of visible light in nanometers: "))

colour = ""

if wavelength >= 350 and wavelength < 450:
	colour = "violet"
elif wavelength >= 450 and wavelength < 495:
	colour = "blue"
elif wavelength >= 495 and wavelength < 570:
	colour = "green"
elif wavelength >= 570 and wavelength < 590:
	colour = "yellow"
elif wavelength >= 590 and wavelength < 620:
	colour = "orange"
elif wavelength >= 620 and wavelength <= 750:
	colour = "red"
	
if colour != "":
	print("This wavelength is the colour {}.".format(colour))
else:
	print("This wavelength is outside the spectrum of visible light.")