#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 01:47:38 2019

@author: meyerhof
"""

import random



def coin_flipper():
    
    options = ['H', 'T']
    flippers = ''
    
    while True:
        flip = random.choice(options)
        flippers = flippers + flip
        
        if len(flippers) >= 3:
            if ( flippers[-3] == flippers[-2] == flippers[-1] ):
                break
            else:
                continue
    return flippers




results = []
suma = 0

for i in range(10):
    results.append(coin_flipper())
    suma += len(results[i])
    print(results[i], "(%d)" %len(results[i]))

average_flips = suma/10    

print ("On average %d flips" %average_flips)
    
    

    