# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:38:47 2017

@author: Kenny
"""

def findKey(dInput,strInput):
    key=dInput.keys()
    val=dInput.values()
    output=[]
    for i in range(0,len(key)):
        if val[i]==strInput:
            output.append(key[i])
    output.sort()
    print output
    return output
    
dInput = {1:'singapore', 20:'china', 4:'japan', 5:'china', 10:'japan'}
findKey(dInput, 'china')# returns [5, 20]
findKey(dInput, 'korea')# returns []

    