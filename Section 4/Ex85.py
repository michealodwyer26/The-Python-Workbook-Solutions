#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:54:14 2019

@author: meyerhof
"""

def main(): 
    print("Ordinal Numbers, equivalence")
    print("1 - First")
    print("2 - Second")
    print("3 - Third")
    print("4 - Fourth")
    print("5 - Fifth")
    print("6 - Sixth")
    print("7 - Seventh")
    print("8 - Eigth")
    print("9 - Nineth")
    print("10 - Tenth")
    print("11 - Eleventh")
    print("12 - Twelfth")

main()






def cardinalto_ordinal(cardinal):
       
    while True: 
        if cardinal != int(cardinal): 
            print("Su número no es un número cardinal")
            cardinal = input("Ingrese un número cardinal: ")
        else:
            break
    if (cardinal < 1) and (cardinal > 12): 
        print("")
    else: 
        if cardinal == 1:
            print("First")
        elif cardinal == 2:
            print("Second")
        elif cardinal == 3:
            print("Third")
        elif cardinal == 4:
            print("Fourth")
        elif cardinal == 5:
            print("Fifth")
        elif cardinal == 6:
            print("Sixth")
        elif cardinal == 7:
            print("Seventh")
        elif cardinal == 8:
            print("Eigth")
        elif cardinal == 9:
            print("Nineth")
        elif cardinal == 10:
            print("Tenth")
        elif cardinal == 11:
            print("Eleventh")
        elif cardinal == 12:
            print("Twelfth")
        
    
cardinalto_ordinal(6)
        

cardinalto_ordinal(-3)