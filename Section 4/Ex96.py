#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 03:48:42 2019

@author: meyerhof
"""

def checkPassword(password): 
    has_upper = False
    has_lower = False
    has_num = False
    
    for ch in password: 
        if ch >= 'A' and ch <= 'Z': 
            has_upper = True
        elif ch >= 'a' and ch <= 'z': 
            has_lower = True
        elif ch >= '0' and ch <= '9':    
            has_num = True
    
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False

def main(): 
    p = input("Ingrese Contraseña: " )
    if checkPassword(p): 
        print("La contraseña es buena")
    else: 
        print("La contraseña es débil")

if __name__ == "__main__": 
    main()