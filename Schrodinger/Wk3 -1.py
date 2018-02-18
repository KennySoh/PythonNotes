# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 18:53:08 2017

@author: yang
"""

def fact(n):
	# Write here
    k=n-1
    while k>1:
        n=n*k
        k=k-1
    return n
    
print 'fact (3)'
ans=fact (3)
print ans
print 'fact (5)'
ans=fact (5)
print ans
print 'fact (4)'
ans=fact (4)
print ans
print 'fact (1)'
ans=fact (1)
print ans