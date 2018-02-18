# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:13:36 2017

@author: yang
"""



import scipy.constants as c
import numpy as np 
import math as m
a=c.physical_constants['Bohr radius'][0]

# Put all other functions here
def l00(x):
	# Write here
     return 1
def l10(x):
    return 1
def l20(x):
    return 2
def l30(x):
    return 6
def l01(x):
    return int(-x+1)
def l11(x):
    return int((-x+1+1)*2)
def l21(x):
    return int((-x+2+1)*6)
def l31(x):
    return int((-x+3+1)*24)
def l02(x):
    return int((0.5*(x*x-4*x+2))*2)
def l12(x):
    return int((0.5*(x*x-6*x+6))*6)
def l22(x):
    return int((0.5*(x*x-8*x+12))*24)
def l32(x):
    return int((0.5*(x*x-10*x+20))*120)
def l03(x):
    return int(((1/6)*((-1*x**3)+9*x*x-18*x+6))*6)
def l13(x):
    return int(((1/6)*((-1*x**3)+12*x*x-36*x+24))*24)
def l23(x):
    return int(((1/6)*((-1*x**3)+15*x*x-60*x+60))*120)
def l33(x):
    return int(((1/6)*((-1*x**3)+18*x*x-90*x+120))*720)

def assoc_laguerre(p,qmp):
    if p==0 and qmp==0:
        return l00
	# Continue here
    if p==1 and qmp==0:
        return l10
    if p==2 and qmp==0:
        return l20
    if p==3 and qmp==0:
        return l30
    if p==0 and qmp==1:
        return l01
    if p==1 and qmp==1:
        return l11
    if p==2 and qmp==1:
        return l21
    if p==3 and qmp==1:
        return l31
    if p==0 and qmp==2:
        return l02
    if p==1 and qmp==2:
        return l12
    if p==2 and qmp==2:
        return l22
    if p==3 and qmp==2:
        return l32
    if p==0 and qmp==3:
        return l03
    if p==1 and qmp==3:
        return l13
    if p==2 and qmp==3:
        return l23
    if p==3 and qmp==3:
        return l33
        
def factorial(n):
    if n == 0:
        return 1
    else:
        return m.factorial(n)   

def radial_wave_func(n,l,r):
	# Write here
    p=2*l+1
    qmp=n-l-1
    lfunc=assoc_laguerre(p,qmp)
    y=lfunc((2*r)/(n*a))
    R1=np.sqrt((8.0/(n)**3)*(factorial(n-l-1))/(2.0*n*((factorial(n+l))**3)))
    R2=np.exp(-r/(n*a))*((2*r)/(n*a))**l
    R=R1*R2*y
    return round(R,5)
 


ans=radial_wave_func(2,1,a)
print ans

ans=radial_wave_func(3,1,2*a)
print ans
 


  

