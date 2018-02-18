# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 21:30:37 2017

@author: yang
"""

import scipy.constants as c


def energy_n(n):
	# returns energy in eV
	# page 149, Eq. 4.7
     n=float(n)
     E=(-c.m_e*c.e**4)/(8*(c.epsilon_0**2)*(c.Planck**2))/(c.e)*(1/n**2)
     return round(E,5)
