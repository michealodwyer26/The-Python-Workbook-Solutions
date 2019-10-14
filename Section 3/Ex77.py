#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:44:16 2019

@author: meyerhof
"""

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)): 
        decimal = decimal + int(binary[i])* 2**(len(binary)- i - 1)
    return decimal


binary = input("Ingrese el número binario que desea convertir: ")

i = 0
while i < len(binary): 
    if (binary[i] != "0") and (binary[i] != "1"):
        print("El valor ingresado no es un número binario")
        binary = input("Ingrese el número binario que desea convertir: ")
        i = 0
    else: 
        i = i+1

print(binary_to_decimal(binary))




    