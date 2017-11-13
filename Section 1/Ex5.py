oneLitreOrLess = int(input("How many bottles have one litre or less: "))
moreThanOneLitre = int(input("How many bottles have more than one litre: "))

refund = (oneLitreOrLess * 0.10) + (moreThanOneLitre * 0.25)

print("The refund for returning these containers is ${0:.2f}.".format(refund))