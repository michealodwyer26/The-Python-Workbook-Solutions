airTemp = float(input("Please enter an air temperature: "))
windSpeed = float(input("Please enter the corresponding wind speed: "))

WCI = 13.12 + (0.6215*airTemp) - (11.37*(windSpeed**0.16)) + (0.3965*airTemp*(windSpeed**0.16))

print("The WCI (Wind Chill Index) is {}.".format(WCI))