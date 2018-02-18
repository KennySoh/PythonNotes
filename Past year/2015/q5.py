# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:49:30 2017

@author: Kenny
"""

class Square(object):
    def __init__(self,x=0,y=0,sideLength=1.0):
        self.x=x
        self.y=y
        self.sideLength=sideLength
    def getCenter(self):
        return (self.x,self.y)
    def getSideLength(self):
        return self.sideLength
    def getArea(self):
        return self.sideLength**2
    def getPerimeter(self):
        return self.sideLength*4
    def containPoint(self,px,py):
        if px<=(self.x+self.sideLength/2)and px>=(self.x-self.sideLength/2):
            if py<=(self.x+self.sideLength/2)and py>=(self.x-self.sideLength/2):
                return True
        return False
    def containSquare(self,inSquare):
        if inSquare.x+inSquare.sideLength/2<=self.x+self.sideLength/2:
            if inSquare.x-inSquare.sideLength/2>=self.x-self.sideLength/2:
                if inSquare.y+inSquare.sideLength/2<=self.y+self.sideLength/2:
                    if inSquare.y-inSquare.sideLength/2>=self.y-self.sideLength/2:
                        return True
        return False
s=Square(x=1,y=1,sideLength=2.0)
print s.getCenter()
#(1, 1)
print s.getSideLength()
#2.0
print s.getArea()
#4.0
print s.getPerimeter()
#8.0
print s.containPoint(0,0)
#True
print s.containPoint(0,-0.5)
#False
print s.containPoint(1,1.5)
#True
print s.containSquare( Square(x=1.5, y = 1, sideLength = 1))
#True
print s.containSquare( Square(x=1.5, y = 1, sideLength = 1.1))
#False
s2 = Square()
print s2.getCenter()
#(0, 0)
print s2.getSideLength()
#1.0
print s2.getPerimeter()
#4.0