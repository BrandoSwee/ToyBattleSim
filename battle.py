# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:21:53 2022

@author: Brandon
"""

from Individual import Individual

#########################################
### This function will return a 1 or 2.
### 1 means individual 1 won and 2 means individual 2 won.
def battle(indi1, indi2):
    stats1 = indi1.getStats()
    stats2 = indi2.getStats()
    target1 = None
    target2 = None
    ########################
    ## setup for stat to target for attacks
    if(indi1.target == 'D'):
        target1 = 4
    else:
        target1 = 5
    if(indi2.target == 'D'):
        target2 = 4
    else:
        target2 = 5
    ####################
    ### Speed check
    # extra will show how many extra attacks an individual gets.
    extra = 0
    # Shows which individual acts first
    whoFirst = None
    # indi1 is faster
    if(stats1[2] > stats2[2]):
        whoFirst = 1
        temp = stats1[2] - stats2[2]
        if(temp < 6):
            extra = 0
        elif(temp < 16):
            extra = 1
        else:
            extra = 3
    # indi2 is faster
    elif(stats2[2] > stats1[2]):
        whoFirst = 2
        temp = stats2[2] - stats1[2]
        if(temp < 6):
            extra = 0
        elif(temp < 16):
            extra = 1
        else:
            extra = 3
    # equal speed
    else:
        # skill
        if(stats1[3] > stats2[3]):
            whoFirst = 1
        elif(stats2[3] > stats1[3]):
            whoFirst = 2
        else:
            # atk
            if(stats1[1] > stats2[1]):
                whoFirst = 1
            elif(stats2[1] > stats1[1]):
                whoFirst = 2
            else:
                # def
                if(stats1[4] > stats2[4]):
                    whoFirst = 1
                elif(stats2[4] > stats1[4]):
                    whoFirst = 2
                else:
                    # res
                    if(stats1[5] > stats2[5]):
                        whoFirst = 1
                    elif(stats2[5] > stats1[5]):
                        whoFirst = 2
                    else:
                        # hp
                        if(stats1[0] > stats2[0]):
                            whoFirst = 1
                        elif(stats2[0] > stats1[0]):
                            whoFirst = 2
                        else:
                            if(indi1.target == 'D' and indi2.target == 'D'):
                                return 1
                            elif(indi1.target == 'R' and indi2.target == 'R'):
                                return 1
                            elif(indi1.target == 'D' and indi2.target == 'R'):
                                whoFirst = 1
                            else:
                                whoFirst = 2
    #print(extra, whoFirst)
    ###########################################################
    # Skill check
    if(stats1[3] > stats2[3] + 5):
        if(stats1[3] > stats2[3] + 15):
            smallList = [[stats2[1],1],[stats2[2],2],[stats2[3],3],[stats2[4],4],[stats2[5],5]]
            smallList.sort()
            target1 = smallList[0][1]
        else:
            if(stats2[4] > stats2[5]):
                target1 = 5
            else:
                target1 = 4
                ## Being equal will mean nothing here.
    elif(stats2[3] > stats1[3] + 5):
        if(stats2[3] > stats1[3] + 15):
            smallList = [[stats1[1],1],[stats1[2],2],[stats1[3],3],[stats1[4],4],[stats1[5],5]]
            smallList.sort()
            target2 = smallList[0][1]
        else:
            if(stats1[4] > stats1[5]):
                target2 = 5
            else:
                target2 = 4
    
    #print(target1, target2)
    ###################
    # Def check
    #Defbuff = 0
    Defbuff1 = 0
    Defbuff2 = 0
    if(stats1[4] > stats2[4] + 10):
        #Defbuff = 1
        Defbuff1 = round(stats1[4] * 0.2)
    elif(stats2[4] > stats1[4] + 10):
        #Defbuff = 2
        Defbuff2 = round(stats2[4] * 0.2)
    #print(Defbuff1, Defbuff2)
    ###################
    # Res check
    #ResRed = 0
    ResRed1 = 0
    ResRed2 = 0
    if(stats1[5] > stats2[5] + 10):
        #ResRed = 1
        ResRed1 = round(stats1[5] * 0.2)
    elif(stats2[5] > stats1[5] + 10):
        #ResRed = 2
        ResRed2 = round(stats2[5] * 0.2)
    #print(ResRed1, ResRed2)
    #####################
    hp1 = stats1[0]
    hp2 = stats2[0]
    #print(hp1, hp2)
    damage1 = stats1[1] + Defbuff1 - ResRed2 - stats2[target1]
    damage2 = stats2[1] + Defbuff2 - ResRed1 - stats1[target2]
    #print(stats1[1], Defbuff1, ResRed2, stats2[target1])
    #print(stats2[1], Defbuff2, ResRed1, stats1[target2])
    #print(damage1, damage2)
    
    if(damage1 < 1):
        damage1 = 1
    if(damage2 < 1):
        damage2 = 1
    #print(damage1, damage2)
    if(whoFirst == 1):
        while True:
            #print(hp1, hp2)
            hp2 = hp2 - damage1
            if(hp2 <= 0):
                return 1
            if(extra == 3):
                hp2 = hp2 - damage1
                if(hp2 <= 0):
                    return 1
            
            hp1 = hp1 - damage2
            if(hp1 <= 0):
                return 2
            
            if(extra > 0):
                hp2 = hp2 - damage1
                if(hp2 <= 0):
                    return 1
            if(extra == 3):
                hp2 = hp2 - damage1
                if(hp2 <= 0):
                    return 1
    else:
        while True:
            hp1 = hp1 - damage2
            if(hp1 <= 0):
                return 2
            if(extra == 3):
                hp1 = hp1 - damage2
                if(hp1 <= 0):
                    return 2
            
            hp2 = hp2 - damage1
            if(hp2 <= 0):
                return 1
            
            if(extra > 0):
                hp1 = hp1 - damage2
                if(hp1 <= 0):
                    return 2
            if(extra == 3):
                hp1 = hp1 - damage2
                if(hp1 <= 0):
                    return 2
    
    #print(stats2)
    ## 0 indicates an error?
    return 0


if __name__ == "__main__":
                     ##hp,atk,spd,sk,def,res
    #obj1 = Individual([30,30,30,30,30,30], 0, 'D')
    #obj2 = Individual([30,30,20,30,29,41], 0, 'R')
    #obj1 = Individual([50,45,0,5,50,30], 0, 'D')
    #obj2 = Individual([20,45,16,21,48,30], 0, 'R')
    obj1 = Individual([27,26,33,27,40,27], 0, 'D') #D-R changes alot here
    obj2 = Individual([38,28,50,32,32,0], 0, 'D') 
    #print(obj1.getStats())
    winner = battle(obj1, obj2)
    print(winner)
    print(obj1.getStats())
    print(obj2.getStats())