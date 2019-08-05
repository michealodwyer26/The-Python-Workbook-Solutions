#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:15:08 2019

@author: meyerhof
"""

def nextPrime(n):
    while True: 
        if n < 0: 
            print("www")
            print("El número no es un entero positivo")
            n = float(input("Ingrese un número entero positivo: "))
        elif n != int(n): 
            print("El número no es un entero positivo")
            n = float(input("Ingrese un número entero positivo: "))
        else: 
            break
    n = int(n)
    n = n+1
    while True:
        for i in range(2,n): 
            if n%i == 0: 
                n = n+1
                break
        else: 
            print("El primero primo más grande que el número ingresado es: ", n)
            break

def main():
    number = float(input("Ingrese un número entero positivo: "))
    nextPrime(number)

main()
