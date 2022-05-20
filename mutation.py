# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:37:46 2022

@author: Brandon
"""
import random
import copy

def majorMutation(indilis, IndistatCap):
    indilist = copy.deepcopy(indilis)
    num = -1
    number = 0
    while True:        
        num = random.randint(0,5)
        number = indilist[num]
        if(number != 0):
            break
    #Note can get duplicate if hp = 1 and hp is picked
    num2 = random.randint(1,number)
    #print(num, num2)
    valsToAdd = 0
    ## Need 1 hp
    if(num == 0 and num2 == number):
        indilist[num] = 1
        valsToAdd = num2 - 1
    else:
        indilist[num] = indilist[num] - num2
        valsToAdd = num2
    AddedVals = 0
    while True:
        if(valsToAdd == AddedVals):
            break
        num3 = random.randint(0,5)
        if(num3 != num):
            if(indilist[num3] != 60):
                indilist[num3] = indilist[num3] + 1
                AddedVals = AddedVals + 1
    
    return indilist
                
def indiMutation(indilis, IndistatCap):
    indilist = copy.deepcopy(indilis)
    # tried 2-5 but changed to 2-4
    statsToChange = random.randint(2,4)
    statsSelected = []
    while True:
        if(len(statsSelected) == statsToChange):
            break
        num = random.randint(0,5)
        if(num not in statsSelected):
            statsSelected.append(num)    
    totalVals = 0
    newVals = []
    numberOfStatsSelected = len(statsSelected)
    ## Needs to be sorted for the hp check
    statsSelected.sort()
    for i in range(numberOfStatsSelected):
        newVals.append(0)
        totalVals = totalVals + indilist[statsSelected[i]]
    ValsAdded = 0
    
    ## Forcing 1 hp
    if(statsSelected[0] == 0):
        newVals[0] = newVals[0] + 1
        ValsAdded = ValsAdded + 1
    
    while True:
        if(ValsAdded == totalVals):
            break
        num = random.randint(0,numberOfStatsSelected -1)
        
        if(newVals[num] < IndistatCap):
            newVals[num] = newVals[num] + 1
            ValsAdded = ValsAdded + 1
    #print(statsToChange, ValsAdded, statsSelected)
    #print(indilist)
    for i in range(numberOfStatsSelected):
        indilist[statsSelected[i]] = newVals[i]
    #print(indilist)
    
    return indilist    
        
if __name__ == "__main__":
    p = [10,30,0,50,60,30]
    e = indiMutation(copy.deepcopy(p), 60)
    n = majorMutation(copy.deepcopy(p), 60)
    print(p)
    print(e)
    print(n)