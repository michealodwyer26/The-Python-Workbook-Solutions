#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 05:44:13 2019

@author: meyerhof
"""

def create_file(): 
    out_file = input("Ingrese el nombre del archivo a numerar: ")
    filename = input("Ingrese el nombre del nuevo archivo numerado: ")
    
    out_f = open(filename, 'w+')
    f = open(out_file)
    
    line = f.readline()
    i = 1
    while line: 
        s = str(i) + ", " + line
        i = i+1
        out_f.write(s)
        line = f.readline()

create_file()