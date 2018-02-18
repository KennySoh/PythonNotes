# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 21:41:28 2017

@author: yang
"""

def l00(x):
	# Write here
     return 1
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
    if qmp==0:
        return l00
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
 
 
#Do not edit anything below this line
def test(p,qmp,x):
	f=assoc_laguerre(p,qmp)
	return f(x)
 
 
print 'f=assoc_laguerre(0,0)'
print 'f(1)'
f=assoc_laguerre(0,0)
ans=f(1)
print ans


print 'f=assoc_laguerre(1,1)'
print 'f(1)'
f=assoc_laguerre(1,1)
ans=f(1)
print ans
print 'f=assoc_laguerre(2,2)'
print 'f(1)'
f=assoc_laguerre(2,2)
ans=f(1)
print ans
print 'f=assoc_laguerre(2,2)'
print 'f(0)'
f=assoc_laguerre(2,2)
ans=f(0)
print ans