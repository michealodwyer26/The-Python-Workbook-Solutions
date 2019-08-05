#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 01:43:51 2019

@author: meyerhof
"""


def check_spell (word, simb_used, i=0, spell=''):
    word = word.casefold()
    
    if word[i].capitalize() in simb_used: 
        spell += word[i].capitalize()
        i += 1
        if i == len(word):
            print(spell)
            return True
        else: 
            return check_spell(word, simb_used, i, spell)
    elif (word[i]+word[i+1]).capitalize() in simb_used: 
        spell += (word[i]+word[i+1]).capitalize()
        i += 2
        if i == len(word): 
            print(spell)
            return True
        else: 
            return check_spell(word, simb_used, i, spell)
    else: 
        return False
    
    
simbs = ['Si','Li','C','O','N']
word = "silicon"

check_spell(word, simbs)