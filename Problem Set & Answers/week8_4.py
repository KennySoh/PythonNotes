# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:27:16 2017

@author: Kenny
"""

class Line:
    def __init__(self,c0,c1):
        self.c0=float(c0)
        self.c1=float(c1)
    
    def __call__(self,x):
        y=self.c0+self.c1*x
        return round(y,2)
    
    def table(self,L,R,n):
        d=(R-L)/float(n-1)
        
        if L==R:
            n=1
        if n==0:
            return "Error in printing table"
        out=""
        for i in range(0,n):
            x=L+i*d
            y=self(x)
            out+="%10.2f%10.2f"%(x,y)+"\n"
        return out
        
g=Line(1,2)
print g(2)
print g.table(1,5,4)
"""
l=Line(-1,2)
print l(2)
print l.table(-1,5,10)

l=Line(3,4)
print l(2)
print l.table(1,5,15)

l=Line(3,4)
print l(2)
print l.table(1,1,15)

l=Line(3,4)
print l(2)
print l.table(1,5,0)

import numpy as np

class Line():
    def __init__(self,c_0,c_1):
        self.c_0 = c_0
        self.c_1 = c_1
    def __call__(self,x):
        return float(self.c_0+self.c_1*x)
    
    def table(self,L,R,n):
        if L==R:
            n=1
        xx=np.linspace(L,R,n)
        retval = ""
        for num in xx:
            retval = retval + "%10.2f%10.2f\n"%(num,self(num))
        if retval == "":
            return "Error in printing table"
        else:
            return retval
line=Line(3,4)
print line(2)
    
print line.table(1,1,15)

"""