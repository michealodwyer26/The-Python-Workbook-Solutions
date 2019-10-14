#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 01:25:09 2019

@author: meyerhof
"""

def wrong_input_handling(data, name_variable=''):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número")
            data = input("Ingrese un número positivo: ")
            continue
        if data < 0:
            print("Un número complejo. El número complejo correspondiente a la raíz de este número negativo no puede ser calculado por este algoritmo")
            data = input("Ingrese un número positivo: ")
            continue
        #En este ejercicio no se necesita esta restricción
        #elif data != int(data):
        #    print("Su número es decimal. No se acepta")
        #    data = input("Ingrese un entero positivo: ")
        #    continue
        else:
            data = float(data)
            break
        
    return data


def square_root(number, guess=1):

    number = wrong_input_handling(number)
    
    if number == 0:
        return 0
    elif number < 0: 
        return 
    else:    
        if abs(guess**2 - number) < 10**(-12)*number:
            return guess
        else:
            guess = (guess + (number/guess))/2
            return square_root(number, guess)
    
number = input("Ingrese el número a buscar la raíz: ")

print("La raíz aproximada es: ", square_root(number))
