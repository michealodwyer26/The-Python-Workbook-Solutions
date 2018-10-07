print("Celsius\t | Fahrenheit")

for celsiusTemp in range(0, 101, 10):
	fahrenheitTemp = (celsiusTemp * 9/5) + 32
	
	print("{}\t | {}".format(celsiusTemp, fahrenheitTemp))