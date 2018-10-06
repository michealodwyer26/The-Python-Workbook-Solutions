frequency = float(input("Enter a frequency: "))

category = ""

if frequency < 3e9:
	category = "radio waves"
elif frequency >= 3e9 and frequency < 3e12:
	category = "microwaves"
elif frequency >= 3e12 and frequency < 4.3e14:
	category = "infrared light"
elif frequency >= 4.3e14 and frequency < 7.5e14:
	category = "visible light"
elif frequency >= 7.5e14 and frequency < 3e17:
	category = "ultraviolet light"
elif frequency >= 3e17 and frequency < 3e19:
	category = "x-rays"
elif frequency >= 3e19:
	category = "gamma rays"
	
if category != "":
	print("This frequency is in the '{}' category.".format(category))
else:
	print("Invalid frequency entered.")