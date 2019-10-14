#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 04:48:19 2019

@author: meyerhof
"""

def hex2int(hexa): 
    H = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    h = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    decimal = 0
    
    while True: 
        for i in hexa:
            if  (i in h) or (i in H):
                continue
            else: 
                print("Acaba de ingresar algo no reconocible como número hexadecimal")
                hexa = input("Ingrese un número en formato hexadecimal: ")
                break
        else: 
            break
    
    for i in range(len(hexa)):
        
        exp = len(hexa) - i -1
        if hexa[i] in h: 
            value = h.index(hexa[i])
        elif hexa[i] in H: 
            value = h.index(hexa[i])
        decimal = decimal + value*16**exp
        
    return decimal 

def int2hex(inter):
    while True: 
        try:
            inter = int(inter)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número entero")
            inter = input("Ingrese un número positivo entre 0 y 15: ")
            continue
        else:
            inter = int(inter)
            break
    h = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return h[inter]
    