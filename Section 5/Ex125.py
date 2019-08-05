#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 05:14:01 2019

@author: meyerhof
"""

def isSublist(larger, smaller): 
    
    if smaller == []: 
        return True
    elif smaller[0] not in larger: 
        return False
    else: 
        start = larger.index(smaller[0])
        
        for i in range(len(smaller)): 
            if smaller[i] == larger[start+i]: 
                continue
            else: 
                return False
        else: 
            return True

def main(): 

    lar = [1,2,3,4,'a','f',23,4,6,232,4]
    small = [123123]
    print(lar)
    print(small)
    print("La Lista pequeña es sublista de la grande?: ",isSublist(lar, small))
            
    
        
    
    
    
    