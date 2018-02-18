# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:30:45 2017

@author: Kenny
"""

class Coordinate(object):
    def __init__(self,u=0,v=0):
        self.x=u
        self.y=v
    def magnitude(self):
        return (self.x**2+self.y**2) ** 0.5
    def translate(self,dx,dy):
        self.x+=dx
        self.y+=dy
    #def __eq__(self,other) # compare 2 objets and check if same
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False

p1=Coordinate()
print p1.x,p1.y
p2=Coordinate(1,2)
print p1.__eq__(p2)