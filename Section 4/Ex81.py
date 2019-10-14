#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 02:43:30 2019

@author: meyerhof
"""
import math as m

def pitágoras(cateto_a, cateto_b):
    
    cateto_a = wrong_input_handling(cateto_a, '(Cateto A)')
    cateto_b = wrong_input_handling(cateto_b, '(Cateto B)')
    
    hypotenuse = m.sqrt(cateto_a**2 + cateto_b**2)
    print(hypotenuse)
    return hypotenuse

def wrong_input_handling(data, variable=''):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número %s" % variable )
            data = input("Ingrese un número positivo: ")
            continue
        if data <= 0:
            print("Su número es cero o negativo. No se acepta %s" % variable)
            data = input("Ingrese un número positivo: ")
            continue
        #En este caso en particular la restricción a número entero no es necesaria.
        #elif data != int(data):
        #    print("Su número es decimal. No se acepta%s" % variable )
        #    data = input("Ingrese un entero positivo: ")
        #    continue
        else:
            data = float(data)
            break
        
    return data

cat_a = input("Ingrese el Cateto A: ")
cat_b = input("Ingrese el Cateto B: ")

pitágoras(cat_a, cat_b)

