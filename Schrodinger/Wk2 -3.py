# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 21:31:15 2017

@author: yang
"""

import scipy.constants as c

def radToDeg(rad):
	#Write your answer here
     rad=float(rad)
     deg=rad*180/c.pi
     return round(deg,5)
     
