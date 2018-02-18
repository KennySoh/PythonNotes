# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 21:31:17 2017

@author: yang
"""

import numpy as np 
import math as m
def sphericalToCartesian(r,theta,phi):
	# Write here
     x=round(r*np.sin(theta)*np.cos(phi))
     y=round(r*np.sin(theta)*np.sin(phi))
     z=round(r*np.cos(theta))
     return (x,y,z)
     
print sphericalToCartesian(3.0,np.pi/2.0,np.pi/2.0)
