#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:06:10 2019

@author: meyerhof
"""

def precedence(operation):
    operation = operation.strip()
    if (operation == '+') or (operation == '-'): 
        return 1
    elif (operation == '*') or (operation == '/'): 
        return 2
    elif (operation == '^'):
        return 3
    else: 
        return -1
    
    
def main():    
    op = input("Ingrese el símbolo de la operación que desea evaluar: ")

    result = precedence(op)
    if result == -1: 
        print("El símbolo ingresado no es una operación válida")
    else: 
        print(result)
        
main()
