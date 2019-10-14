#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 01:51:11 2019

@author: meyerhof
"""



def decomp(code, decode=[], i=0):
    
    letter = code[i]
    rep = code[i+1]
    for reps in range(rep): 
        decode.append(letter)
    
    i += 2
    if i < len(code):
        decomp(code, decode, i)
    else: 
        print(decode)




def main(): 
    code = ['A',12,'B',4,'A',6,'B',3]
    print(code)
    print()
    decomp(code)
    
if __name__ == "__main__":
    main()
    