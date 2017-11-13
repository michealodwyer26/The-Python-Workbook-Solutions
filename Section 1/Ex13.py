cents = int(input("Please enter a number of cents: "))

toonies = int(cents / 200) # A toonie is a Canadian name for a $2 coin
cents -= toonies * 200

loonies = int(cents / 100) # A toonie is a Canadian name for a $1 coin
cents -= loonies * 100

quarters = int(cents/25) # A quarter is 25 cents
cents -= quarters * 25

dimes = int(cents/10) # A dime is 10 cent
cents -= dimes * 10

nickels = int(cents/5) # A nickel is 5 cent

pennies = cents

print("The change using the smallest amount of change is...")
print("{} toonies, {} loonies, {} quarters, {} dimes, {} nickels, {} pennies".format(toonies, loonies, quarters, dimes, nickels, pennies))
