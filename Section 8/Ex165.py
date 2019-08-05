#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:27:16 2019

@author: meyerhof
"""


def great_common_div(a, b):
    a = wrong_input_handling(a, '(1° num)')
    b = wrong_input_handling(b, '(2° num)')
    if b == 0:
        return a
    else:
        c = a%b
        return great_common_div(b, c)
        

def wrong_input_handling(data, variable=''):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número %s" % variable )
            data = input("Ingrese un entero positivo: ")
            continue
        if data < 0:
            print("Su número es negativo. No se acepta %s" % variable)
            data = input("Ingrese un entero positivo: ")
            continue
        elif data != int(data):
            print("Su número es decimal. No se acepta%s" % variable )
            data = input("Ingrese un entero positivo: ")
            continue
        else:
            data = int(data)
            break
        
    return data

num_a = input("Ingrese el primer número: ")
num_b = input("Ingrese el segundo número: ")

print(great_common_div(num_a, num_b))