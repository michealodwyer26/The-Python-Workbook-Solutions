#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 06:03:01 2019

@author: meyerhof
"""

from Ej138 import createCard, displayCard
import random as rand

num_of_cards = int(input("Ingrese el número de cartas que desea crear: "))
    
cards_created = []
for i in range(num_of_cards): 
    a = createCard()
    cards_created.append(a)

for i in range(len(cards_created)): 
    print("---")
    print("Card num: ", i+1)
    displayCard(cards_created[i])
    print("___")

input("Press Enter to continue")

def Num_Let(): 
    let = ['B','I','N','G','O']
    winlet = rand.choice(let)
    
    if winlet == "B":
        winum = rand.randint(1,15)
    elif winlet == "I":
        winum = rand.randint(16,30)
    elif winlet == "N":
        winum = rand.randint(31,45)
    elif winlet == "G":
        winum = rand.randint(46,60)
    elif winlet == "O":
        winum = rand.randint(61,75)
    
    return [winlet, winum]

def check_vertical(card): 
    for i in card:
        suma = sum(card[i])
        if suma == 0: 
            break 
    else: 
        return False
    return True

def check_horizontal(card):
    for i in range(5):  #Todas las posiciones
        suma = 0
        for let in card:    #Cada letra. 
            suma = suma + card[let][i]  #Sumo todas las posiciones i, para cada letra => Una horizontal
        if suma == 0: 
            break
    else: 
        return False
    return True

def check_diagonal(card): 
    pos = range(5)
    suma = 0
    
    for i, let in zip(pos, card):
        suma = suma + card[let][i]
    if suma == 0: 
        return True
    else: 
        return False
    
def check_antidiagonal(card): 
    antipos = range(4,-1,-1)
    suma = 0
    
    for i, let in zip(antipos, card):
        suma = suma + card[let][i]
    if suma == 0: 
        return True
    else: 
        return False


def check_cards(card_list):
    
    Winner = False
    
    while Winner == False:
        num_let = Num_Let()
        
        for card in card_list: 
            if num_let[1] in card[num_let[0]]:
                pos = card[num_let[0]].index(num_let[1])
                card[num_let[0]][pos] = 0
                print("---------")
                print(num_let)
                print("Card: ", card_list.index(card)+1)
                displayCard(card)
                print()
                print("---------")
            else: 
                print("---------")
                print(num_let)
                print()
                print("---------")
        
            if (check_horizontal(card) or check_vertical(card) or check_diagonal(card) or check_antidiagonal(card)):
                Winner = True
                Winner_pos = card_list.index(card)
                Winner_card = card
                break 
    
    return [Winner, Winner_card, Winner_pos]

results = check_cards(cards_created)

print()
print("Winner Card is Card: ", results[2]+1)
displayCard(results[1])


        
        
        
        
        
        
        
        
        