#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 02:56:12 2019

@author: meyerhof
"""
def wrong_input_handling(data, variable=''):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número %s" % variable )
            data = input("Ingrese un número positivo: ")
            continue
        if data <= 0:
            print("Su número es negativo o cero. No se acepta %s" % variable)
            data = input("Ingrese un número positivo: ")
            continue
        elif data != int(data):
            print("Su número es decimal. No se acepta%s" % variable )
            data = input("Ingrese un entero positivo: ")
            continue
        else:
            data = int(data)
            break
        
    return data

def sending_cost(amount_items, cost_item=2.95, cost_first=10.95):
    
    amount_items = wrong_input_handling(amount_items, '(Cantidad de Elementos)')    
    
    total_cost = cost_first + cost_item*(amount_items-1)
    
    return total_cost

costo = input("Ingrese la cantidad de elementos comprados: ")

print("El costo del envío es: %f" %sending_cost(costo))

