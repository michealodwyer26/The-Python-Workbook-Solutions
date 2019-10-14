#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:52:43 2019

@author: meyerhof
"""

def wrong_input_handling(data):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número")
            data = input("Ingrese un entero positivo: ")
            continue
        if data < 0:
            print("Su número es negativo. No se acepta")
            data = input("Ingrese un entero positivo: ")
            continue
        elif data != int(data):
            print("Su número es decimal. No se acepta")
            data = input("Ingrese un entero positivo: ")
            continue
        else:
            data = int(data)
            break
        
    return data

def prime_factorization(n):
    n = wrong_input_handling(n)
    factor = 2
    
    while factor <= n: 
        if n%factor == 0:
            print(factor)
            n = n//factor
        else: 
            factor = factor +1

number = input("Ingrese el número que desea factorizar: ")

print(prime_factorization(number))