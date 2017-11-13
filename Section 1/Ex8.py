noOfWigets = int(input("Please enter the amount of widgets: "))
noOfGizmos = int(input("Please enter the amount of gizmos: "))

widgetWeight = 75
gizmoWeight = 112

totalWeight = (noOfWigets * widgetWeight) + (noOfGizmos * gizmoWeight)

print("The total weight of all these widgets and gizmos is {} grams.".format(totalWeight))