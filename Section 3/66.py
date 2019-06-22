grades = []

while True:
    grade = input("Enter an American grade: ")

    points = 0

    if grade == "":
        break
    if grade == "A+":
        points = 4.0
    if grade == "A":
        points = 4.0
    if grade == "A-":
        points = 3.7
    if grade == "B+":
        points = 3.3
    if grade == "B":
        points = 3.0
    if grade == "B-":
        points = 2.7
    if grade == "C+":
        points = 2.3
    if grade == "C":
        points = 2.0
    if grade == "C-":
        points = 1.7
    if grade == "D+":
        points = 1.3
    if grade == "D":
        points = 1.0
    if grade == "F":
        points = 0
    
    grades.append(points)

total = 0 
num = 0
for grade in grades:
    total += grade 
    num += 1

average = total / num 

print("Your grade average is {}.".format(average))