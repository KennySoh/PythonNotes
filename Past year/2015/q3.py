# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:33:12 2017

@author: Kenny
"""

def compTrace(A):
    sum=0.0
    for i in range(0,len(A)):
        sum+=A[i][i]
    return sum
    
A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
print compTrace(A)