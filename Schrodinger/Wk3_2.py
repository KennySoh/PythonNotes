# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 18:53:11 2017

@author: yang
"""

import numpy as np 
#these are the sets of associated Legendre's Polynomial
# taken from Table 4.2, page 138
def p00(theta):
	# Write here
     return 1
def p02(theta):
    return 0.5*(3*np.power(np.cos(theta), 2)-1)
def p12(theta):
    return 3*np.cos(theta)*np.sin(theta)
def p22(theta):
    return 3*np.power(np.sin(theta),2)
def p03(theta):
    return 0.5*(5*np.power(np.cos(theta),3)-3*np.cos(theta))
def p13(theta):
    return 1.5*(5*np.power(np.cos(theta),2)-1)*np.sin(theta)
def p23(theta):
    return 15*np.cos(theta)*np.power(np.sin(theta),2)
def p33(theta):
    return 15*np.power(np.sin(theta),3)
def assoc_legendre(m,l):
    if m==0 and l==0:
        return p00
	#continue here
    if m==0 and l==1:
        return np.cos
    if m==1 and l==1:
        return np.sin
    if m==0 and l==2:
        return p02
    if m==1 and l==2:
        return p12
    if m==2 and l==2:
        return p22
    if m==0 and l==3:
        return p03
    if m==1 and l==3:
        return p13
    if m==2 and l==3:
        return p23
    if m==3 and l==3:
        return p33

     
      
     
     
#Do not edit anything below this line
def test(m,l,x):
	f=assoc_legendre(m,l)
	return f(x)
 
 
 
 