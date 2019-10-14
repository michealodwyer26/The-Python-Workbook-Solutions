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
            print("Su número es negativo. No se acepta %s" % variable)
            data = input("Ingrese un número positivo: ")
            continue
        #EN ESTE CASO NO SE NECESITA LA RESTRICCIÓN A NÚMEROS ENTEROS
        #elif data != int(data):
        #    print("Su número es decimal. No se acepta%s" % variable )
        #    data = input("Ingrese un entero positivo: ")
        #    continue
        else:
            data = float(data)
            break
        
    return data

def taxi_cost(distance, cost_per_distance=0.25, base_cost=4):
    
    distance = wrong_input_handling(distance, '(Distancia)')    
    cost_per_distance = wrong_input_handling(cost_per_distance, '(Costo por Distancia)')
    base_cost = wrong_input_handling(base_cost, '(Costo Base)')
    
    total_cost = distance*cost_per_distance + base_cost
    
    return total_cost

recorrido = input("Ingrese la distancia recorrida: ")

print("El costo del viaje es: %f" %taxi_cost(recorrido))
