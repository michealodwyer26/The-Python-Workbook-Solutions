line = input("Enter 8 bits in binary: ")

while line != "":
    if line.count("1") + line.count("0") != 8:
        print("Not 8 bits")
    elif line.count("1") % 2 == 0:
        print("Parity bit should be 0.")
    else:
        print("Parity bit should be 1")
    line = input("Enter 8 bits in binary: ")
    