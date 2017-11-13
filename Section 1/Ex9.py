amount = float(input("How much money is initially deposited into the savings account: $"))

interestRate = 0.04 # Interest for this savings A/C is 4%

interest = amount * interestRate
amount += interest
print("Balance as of end of Year 1: ${0:0.2f}.".format(amount))

interest = amount * interestRate
amount += interest
print("Balance as of end of Year 2: ${0:0.2f}.".format(amount))

interest = amount * interestRate
amount += interest
print("Balance as of end of Year 3: ${0:0.2f}.".format(amount))