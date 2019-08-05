#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:50:34 2019

@author: meyerhof
"""

def wrong_input_handling(data, name_variable=''):
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

def decimal_to_binary(decimal, binary=''):
    
    decimal = wrong_input_handling(decimal)    
    
    result_div = decimal//2
    rest = decimal%2
    binary_result = str(rest)+binary
    
    if result_div > 0:
        return decimal_to_binary(result_div, binary_result)
    else:
        return binary_result

number = input("Ingrese el número que desea pasar a binario: ")

print(decimal_to_binary(number))

