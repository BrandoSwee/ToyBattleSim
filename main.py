# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:06:52 2022

@author: Brandon
"""

from battle import battle
from Individual import Individual
from mutation import indiMutation, majorMutation
import matplotlib.pyplot as plt
import copy
import random

def main():
    population = 50
    Generations = 300
    #statCap = 165
    #statCap = 180
    #statCap = 200
    #statCap = 230
    statCap = 280
    individualStatCaps = 60
    wantToSeeFinalTourneyOut = False
    wantToSeeFinalPopu = False
    #seed = 41
    #seed = 10293.7
    seed = 456753852951
    random.seed(seed)
    
    if(individualStatCaps * 5 < statCap):
        print("Stat selection is not vaild for the program.")
        return 
    popu = []
    ## Create random starter population
    for i in range(population):
        ## Can't have 0 hp
        indilist = [1,0,0,0,0,0]
        valsAdded = 1
        while True:
            if(valsAdded == statCap):
                break
            num = random.randint(0,5)
            if(indilist[num] != individualStatCaps):
                indilist[num] = indilist[num] + 1
                valsAdded = valsAdded + 1
        num = random.randint(0,1)
        target = 'R'
        if(num == 0):
            target = 'D'
        IndiObj = Individual(indilist, 0, target)
        popu.append(IndiObj)    
    pltx = []
    pltx.append(0)
    pltyhp = []
    totalhp = 0
    pltyatk = []
    totalatk = 0
    pltyspd = []
    totalspd = 0
    pltyskl = []
    totalskl = 0
    pltydef = []
    totaldef = 0
    pltyres = []
    totalres = 0
    longLivingIndis = []
    for i in range(population):
        stats = popu[i].getStats()
        #print(stats)
        totalhp = totalhp + stats[0]
        totalatk = totalatk + stats[1]
        totalspd = totalspd + stats[2]
        totalskl = totalskl + stats[3]
        totaldef = totaldef + stats[4]
        totalres = totalres + stats[5]
    pltyhp.append(totalhp/population)
    pltyatk.append(totalatk/population)
    pltyspd.append(totalspd/population)
    pltyskl.append(totalskl/population)
    pltydef.append(totaldef/population)
    pltyres.append(totalres/population)
    #for i in range(len(popu)):
    #    print(popu[i].getStats(), popu[i].index, popu[i].target)
    
    for i in range(Generations):
        totalhp = 0
        totalatk = 0
        totalspd = 0
        totalskl = 0
        totaldef = 0
        totalres = 0
        popu = RunPopulation(popu, population, individualStatCaps, i, Generations, wantToSeeFinalTourneyOut)
        for j in range(population):
            stats = popu[j].getStats()
            totalhp = totalhp + stats[0]
            totalatk = totalatk + stats[1]
            totalspd = totalspd + stats[2]
            totalskl = totalskl + stats[3]
            totaldef = totaldef + stats[4]
            totalres = totalres + stats[5]
            if(popu[j].counter == 20):
                longLivingIndis.append([copy.deepcopy(popu[j].stats),copy.deepcopy(popu[j].target), copy.deepcopy(popu[j].index)])
        pltyhp.append(totalhp/population)
        pltyatk.append(totalatk/population)
        pltyspd.append(totalspd/population)
        pltyskl.append(totalskl/population)
        pltydef.append(totaldef/population)
        pltyres.append(totalres/population)
        pltx.append(i + 1)
        
    #plt.plot(pltx, [pltyhp,pltyatk,pltyspd,pltyskl,pltydef,pltyres])
    #print(pltx)
    if(wantToSeeFinalPopu):
        for i in range(len(popu)):
            print(i,popu[i].getStats(), popu[i].index, popu[i].target)
    print("Listing of individuals' stat spreads that lasted for 20+ populations. \nDuplicates may appear\nIts stats, target, and population the individual appeared.")
    for i in range(len(longLivingIndis)):
        print(longLivingIndis[i])
    plt.plot(pltx, pltyatk, label='atk')
    plt.plot(pltx, pltyspd, label='spd')
    plt.plot(pltx, pltyskl, label='skl')
    plt.legend()
    plt.title('Offensive stats over time')
    plt.show()
    plt.clf()            
    plt.plot(pltx, pltyhp, label='hp')
    plt.plot(pltx, pltydef, label='def')
    plt.plot(pltx, pltyres, label='res')
    plt.legend()
    plt.title('Defensive stats over time')
    plt.show()
    plt.clf()  
    print("Ending averages for the population")
    print("  hp    atk   spd   skl   def   res")
    print("[",round(pltyhp[Generations],2),round(pltyatk[Generations],2),round(pltyspd[Generations],2),round(pltyskl[Generations],2),round(pltydef[Generations],2),round(pltyres[Generations],2),"]")
    
        
def RunPopulation(popu, population, individualStatCaps, itera,Generation, yupp):
    for g in range(population):
        num = random.randint(0,1)
        mutatedStats = []
        #if(itera == 499 and g == 3):
        #    print(num)
        #    print(popu[g].stats)
        if(num == 1):
            mutatedStats = indiMutation(popu[g].stats,individualStatCaps)
        else:
            mutatedStats = majorMutation(popu[g].stats,individualStatCaps)
        num = random.randint(0,1)
        target = 'R'
        if(num == 0):
            target = 'D'
        IndiObj = Individual(mutatedStats, itera + 1, target)
        #print(IndiObj.stats)
        popu.append(IndiObj)
        
    #wins = [0]*len(popu)
    wins = []
    
    for h in range(len(popu)):
        wins.append([0, h])
    
    for m in range(len(popu) - 1):
        for n in range(m+1,len(popu),1):
            winner = battle(popu[m], popu[n])
            if(winner == 1):
                #popu[i] won
                wins[m][0] = wins[m][0] + 1
            else:
                wins[n][0] = wins[n][0] + 1
    
    wins.sort()
    wins.reverse()
    returnPop = []
    for e in range(population):
        returnPop.append(copy.deepcopy(popu[wins[e][1]]))
        returnPop[e].increment()
    if(Generation == itera + 1 and yupp):
        print(wins)
    
    return returnPop   
        
if __name__ == "__main__":
    main()
    #print("WIP")
