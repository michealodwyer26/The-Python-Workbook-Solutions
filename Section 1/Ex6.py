mealAmount =  float(input("Please enter the meal amount exluding tax: $"))

taxRate = 0.23 # VAT is 23% in Ireland
tipPercentage = 0.18 # Tip percentage comes from question
tax = mealAmount * taxRate
tip = mealAmount * tipPercentage

total = mealAmount + tax + tip

print("Tax: ${0:0.2f}.".format(tax))
print("Tip: ${0:0.2f}.".format(tip))
print("Grand TOTAL: ${0:0.2f}.".format(total))