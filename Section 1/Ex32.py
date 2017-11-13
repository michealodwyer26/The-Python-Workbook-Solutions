firstNumber = int(input("Please enter the first number: "))
secondNumber = int(input("Plase enter the second number: "))
thirdNumber = int(input("Please enter the third number: "))

smallest = min(firstNumber, secondNumber, thirdNumber)
largest = max(firstNumber, secondNumber, thirdNumber)
middle = (firstNumber+secondNumber+thirdNumber) - smallest - largest

print("The values ordered smallest to largest is: {}, {}, {}.".format(smallest, middle, largest))