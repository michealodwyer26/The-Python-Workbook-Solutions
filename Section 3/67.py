charges = []

while True:
    age = input("Enter the guest's age: ")

    if age == "":
        break

    charge = 0
    age_int = int(age)
    if age_int <= 2:
        charge = 0
    elif age_int >= 3 and age_int < 12:
        charge = 14
    elif age_int >= 65:
        charge = 18
    else:
        charge = 23
    charges.append(charge)

total = 0.00
for charge in charges:
    total += charge

print("Total for this group is ${:.2f}".format(total))