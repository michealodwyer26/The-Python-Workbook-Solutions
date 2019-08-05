#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 03:29:45 2019

@author: meyerhof
"""

from Ej94 import randomPassword
from Ej96 import checkPassword

def main(): 
    n = 0
    passw = ''
    while not checkPassword(passw): 
        passw = randomPassword()
        n = n+1
    print("Intentos: ", n)
    print("Password: ", passw)
    
main()
        