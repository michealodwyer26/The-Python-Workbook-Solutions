days = int(input("Please enter a number of days: "))
hours = int(input("Please enter a number of hours: "))
minutes = int(input("Please enter a number of minutes: "))
seconds = int(input("Please enter a number of seconds: "))

totalSeconds = seconds
totalSeconds += minutes * 60
totalSeconds += hours * 60 * 60
totalSeconds += days * 60 * 60 * 24

print("The total number of seconds is {}.".format(totalSeconds))