noOfDayOldBreadLoaves = int(input("Please enter the number of day old loves of bread being purchased: "))

dayOldDiscount = 0.60 # 60% discount

regularPrice = noOfDayOldBreadLoaves * 3.49
discountedPrice = noOfDayOldBreadLoaves * (3.49 * dayOldDiscount)

print("Regular price is ${:.2f}.".format(regularPrice))
print("Discounted price is ${:.2f}.".format(discountedPrice))