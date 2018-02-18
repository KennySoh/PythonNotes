# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 21:30:25 2017

@author: yang
"""

import scipy.constants as c

def degToRad(deg):
	# Write your answer
    deg=float(deg)
    rad=deg*c.pi/180
    return round(rad,5)

def radToDeg(rad):
	#Write your answer here
     rad=float(rad)
     deg=rad*180/c.pi
     return round(deg,5)    