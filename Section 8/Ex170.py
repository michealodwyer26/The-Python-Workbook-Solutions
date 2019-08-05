#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:06:27 2019

@author: meyerhof
"""

from itertools import combinations_with_replacement as comb

penny = 0.01
nickel =0.05
dime = 0.1
quarter = 0.25

coins = [ quarter, dime, nickel, penny]
    
def check_coins(amount, num_coins, i=1, gen=True, coins_comb='', iters=0): 
        
    if gen: 
        coins_comb = comb(coins, num_coins)
        iters = len(list(comb(coins, num_coins)))
        gen = False
    actual_comb = next(coins_comb)        
    if amount != round(sum(actual_comb),4): 
        i += 1
        if i > iters: 
            print( False)
        else: 
            return check_coins(amount, num_coins, i,gen, coins_comb, iters)
    else: 
        print(actual_comb)
        return True 
            
print(check_coins(1.4, 7))




        