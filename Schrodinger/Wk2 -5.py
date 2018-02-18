# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 21:31:18 2017

@author: yang
"""

import math as m
def cartesianToSpherical(x, y, z):
	#Write here
     x=float(x)
     y=float(y)
     z=float(z)
     r=round(m.sqrt(x*x+y*y+z*z),5)
     theta=round(m.atan2(m.sqrt(x*x+y*y),z),5)
     phi=round(m.atan2(y,x),5)
     return (r,theta,phi)
     
     
