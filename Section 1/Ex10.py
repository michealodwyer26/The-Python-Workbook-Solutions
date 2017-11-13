import math

a = int(input("Please enter a: "))
b = int(input("Please enter b: "))

sum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
log10 = math.log10(a)
powered = a ** b

print("The sum: {}".format(sum))
print("The difference: {}".format(difference))
print("The product: {}".format(product))
print("The quotient: {}".format(quotient))
print("The remainder: {}".format(remainder))
print("Result of log10a: {}".format(log10))
print("Result of a to the power of b: {}".format(powered))