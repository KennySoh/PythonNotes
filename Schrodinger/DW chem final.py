# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:19:00 2017

@author: yang
"""

import scipy.constants as c


def energy_n(n):
	# returns energy in eV
	# page 149, Eq. 4.7
     n=float(n)
     E=(-c.m_e*c.e**4)/(8*(c.epsilon_0**2)*(c.Planck**2))/(c.e)*(1/n**2)
     return round(E,5)
     
     
def deg_to_rad(deg):
	# Write your answer
    deg=float(deg)
    rad=deg*c.pi/180
    return round(rad,5)
    
def rad_to_deg(rad):
	#Write your answer here
     rad=float(rad)
     deg=rad*180/c.pi
     return round(deg,5)
     
import math as m
def spherical_to_cartesian(r,theta,phi):
	# Write here
     x=round(r*m.sin(theta)*m.cos(phi),5)
     y=round(r*m.sin(theta)*m.sin(phi),5)
     z=round(r*m.cos(theta),5)
     return (x,y,z)
     
def cartesian_to_spherical(x, y, z):
	#Write here
     x=float(x)
     y=float(y)
     z=float(z)
     r = np.sqrt(pow(x,2)+pow(y,2)+pow(z,2))
     theta = m.acos(z/r)
     theta= round(theta,5)
     if x==0:
         if y!=0:
             phi = c.pi/2.0
         else:
             phi=0
     else:
         if y==0:
             if x>0 and z==0:
                 phi =0
             else:
                 phi = c.pi
         else:
             phi = m.atan2(y,x)
             phi = round(phi,5)
     return r,theta,phi
def fact(n):
	# Write here
     f=1
     while n!=0:
         f=f*n
         n=n-1
     return int(f)
     
import numpy as np 
def p00(theta):
    return 1
 
def p01(theta):
    return np.cos(theta)
 
def p02(theta):
    return 0.5*(3*np.cos(theta)**2-1)
 
def p03(theta):
    return 0.5*(5*np.cos(theta)**3-3*np.cos(theta))
 
def p04(theta):
    return 0.125 * (35 * np.cos(theta) ** 4 - 30 * np.cos(theta) ** 2 + 3)
 
def p11(theta):
    return np.sin(theta)
 
def p12(theta):
    return 3*np.sin(theta)*np.cos(theta)
 
def p13(theta):
    return 1.5*np.sin(theta)*(5*np.cos(theta)**2-1)
 
def p14(theta):
    return 2.5 * (7 * np.cos(theta) ** 3 - 3 * np.cos(theta)) * np.sin(theta)
 
def p20(theta):
    return 0.5 * (3 * (np.cos(theta) ** 2) - 1)
 
def p22(theta):
    return 3*np.sin(theta)**2
 
def p23(theta):
    return 15*np.sin(theta)**2*np.cos(theta)
 
def p24(theta):
    return 7.5 * (7 * np.cos(theta) ** 2 - 1) * np.sin(theta) ** 2
 
def p33(theta):
    return 15*np.sin(theta)*(1-np.cos(theta)**2)
 
def p34(theta):
    return 105 * np.cos(theta) * np.sin(theta) ** 3
 
def p43(theta):
    return 105 * np.cos(theta) * np.sin(theta) ** 3
 
def p44(theta):
    return 105 * np.sin(theta) ** 4
 
def assoc_legendre(m,l):
    m=abs(m)
    if m==0 and l==0:
        return p00
    elif m==0 and l==1:
        return p01
    elif m==0 and l==2:
        return p02
    elif m==0 and l==3:
        return p03
    elif m==0 and l==4:
        return p04
    elif m==1 and l==1:
        return p11
    elif m==1 and l==2:
        return p12
    elif m==1 and l==3:
        return p13
    elif m==1 and l==4:
        return p14
    elif m==2 and l==0:
        return p20
    elif m==2 and l==2:
        return p22
    elif m==2 and l==3:
        return p23
    elif m==2 and l==4:
        return p24
    elif m==3 and l==3:
        return p33
    elif m==3 and l==4:
        return p34
    elif m==4 and l==3:
        return p43
    elif m==4 and l==4:
        return p44



def factorial(n):
    if n == 0:
        return 1
    else:
        return m.factorial(n)
        
def angular_wave_func(m,l,theta,phi):
    if m>0:
        e=(-1.0)**m
    if m<=0:
        e=1.0
    soln_1=e*((2*l+1.0)*factorial(l-abs(m))/((4.0*c.pi)*(factorial(l+abs(m)))))**(0.5)
    soln_2=np.cos(m*phi)+np.sin(m*phi)*1.0j         #exp(i*m*phi) eluer formula
    
    pfunc=assoc_legendre(abs(m),l)  #return a funciton (theta)
    soln_3=pfunc(theta)
    soln_total=soln_1*soln_2*soln_3
    soln_total=np.round(soln_total,5)
    return soln_total # <<<m,l,phi   qns 2e
                # complex number 5 dec for both real and imaginary


a=c.physical_constants['Bohr radius'][0]

def l00(x):
    return 1
 
def l01(x):
    return -x+1
 
def l02(x):
    return x*x-4*x+2
 
def l03(x):
    return -x*x*x+9*x*x-18*x+6
 
def l04(x):
    return x ** 4 - 16 * x ** 3 + 72 * x ** 2 - 96 * x +24
 
def l10(x):
    return 1
 
def l11(x):
    return -2*x+4
 
def l12(x):
    return 3*x*x-18*x+18
 
def l13(x):
    return -4*x*x*x+48*x*x-144*x+96
 
def l14(x):
    return 5 * x ** 4 - 100 * x ** 3 + 600 * x ** 2 - 1200 * x + 600
 
def l15(x):
    return -720 * (x - 6)
 
def l20(x):
    return 2
 
def l21(x):
    return -6*x+18
 
def l22(x):
    return 12*x*x-96*x+144
 
def l23(x):
    return -20*x*x*x+300*x*x-1200*x+1200
 
def l24(x):
    return 30 * x ** 4 - 720 * x ** 3 + 5400 * x ** 2 - 14400 * x + 10800
 
def l30(x):
    return 6
 
def l31(x):
    return -24*x+96
 
def l32(x):
    return 60*x*x-600*x+1200
 
def l33(x):
    return -120 * x ** 3 + 2160 * x ** 2 - 10800 * x + 14400
 
def l34(x):
    return -210 * x ** 4 + 5880 * x ** 3 - 52920 * x ** 2 + 176400 * x - 176400
 
def l44(x):
    return 1680 * x ** 4 - 53760 * x ** 3 + 564480 * x ** 2 - 2257920 * x + 2822400
 
def l50(x):
    return 120
 
def l51(x):
    return -720 * (x - 6)
 
def l70(x):
    return 5040
 
def assoc_laguerre(p,qmp):
    if p==0 and qmp==0:
        return l00
    elif p==0 and qmp==1:
        return l01
    elif p==0 and qmp==2:
        return l02
    elif p==0 and qmp==3:
        return l03
    elif p==0 and qmp==4:
        return l04
    elif p==1 and qmp==0:
        return l10
    elif p==1 and qmp==1:
        return l11
    elif p==1 and qmp==2:
        return l12
    elif p==1 and qmp==3:
        return l13
    elif p==1 and qmp==4:
        return l14
    elif p==1 and qmp==5:
        return l15
    elif p==2 and qmp==0:
        return l20
    elif p==2 and qmp==1:
        return l21
    elif p==2 and qmp==2:
        return l22
    elif p==2 and qmp==3:
        return l23
    elif p==2 and qmp==4:
        return l24
    elif p==3 and qmp==0:
        return l30
    elif p==3 and qmp==1:
        return l31
    elif p==3 and qmp==2:
        return l32
    elif p==3 and qmp==3:
        return l33
    elif p==3 and qmp==4:
        return l34
    elif p==4 and qmp==4:
        return l44
    elif p==5 and qmp==0:
        return l50
    elif p==5 and qmp==1:
        return l51
    elif p==7 and qmp==0:
        return l70
        

def radial_wave_func(n,l,r):
	# Write here
    p=2*l+1
    qmp=n-l-1
    lfunc=assoc_laguerre(p,qmp)
    y=lfunc((2.0*r)/(n*a))
    R1=np.sqrt((8.0/(n)**3)*(factorial(n-l-1))/(2.0*n*((factorial(n+l))**3)))
    R2=np.exp(-r/(n*a))*((2*r)/(n*a))**l
    R=R1*R2*y
    return np.round(R,5)


ans=radial_wave_func(1,0,a)
print ans

ans=radial_wave_func(1,0,a)
print ans

ans=radial_wave_func(2,1,a)
print ans

ans=radial_wave_func(2,1,2*a)
print ans
             
def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    x=np.linspace(-roa,roa,Nx)
    y=np.linspace(-roa,roa,Ny)
    z=np.linspace(-roa,roa,Nz)
    xx,yy,zz=np.meshgrid(x,y,z)
    vfunc=np.vectorize(cartesian_to_spherical)
    
    roaa, theta, phi=vfunc(xx,yy,zz)
    a=c.physical_constants['Bohr radius'][0]
    r=roaa*a
    rmag=radial_wave_func(n,l,r)
    angumag=angular_wave_func(m,l,theta,phi)
    final=np.absolute(rmag*angumag)**2
    return np.round(xx,5),np.round(yy,5),np.round(zz,5),np.round(final,5)
    
