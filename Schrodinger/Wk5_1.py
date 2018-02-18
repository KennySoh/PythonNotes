from numpy import *
from scipy import *
from scipy.special import *
from sympy import *
from math import *
from matplotlib import *
from scipy.constants import *
import cmath
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def energy_n(n):
    energy = -(((m_e/(2*hbar**2))*(e**2/(4*pi*epsilon_0))**2))*1/n**2
    print energy
    return energy/e
    
def deg_to_rad(d):
    angle = d*2*pi/360
    return round(angle,5)

def rad_to_deg(r):
    angle = r*360/(2*pi)
    return round(angle,5)
    
def spherical_to_cartesian(r,phi,theta): #theta - elevation, phi-azimuth
    theta = float(theta)
    phi = float(phi)
    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(phi)
    return round(x,5),round(y,5),round(z,5)

def cartesian_to_spherical(x,y,z):
    r = sqrt(pow(x,2)+pow(y,2)+pow(z,2))
    theta = acos(z/r)
    if x==0:
        if y!=0:
            phi = pi/2.0
        else:
            phi=0
    else:
        if y==0:
            if x>0 and z==0:
                phi =0
            else:
                phi = pi
        else:
            phi = atan2(y,x)
    return r,round(theta,5),round(phi,5)
    
def fact(b):
    fac= 1
    while b!=0:
        fac = fac*b
        b-=1    
    return int(fac)
    
def p00(th):
    return 1

def p10(th):
    return cos(th)

def p11(th):
    return sin(th)

def p20(th):
    return 0.5*(3*pow(cos(th),2)-1)

def p21(th):
    return 0.5*(6*cos(th)*sin(th))

def p22(th):
    return 3*pow(sin(th),2)

def p30(th):
    return (5*pow(cos(th),2)-3*cos(th))/2

def p31(th):
    return 1.5*sin(th)*(5*pow(cos(th),2)-1)

def p32(th):
    return 15*pow(sin(th),2)*cos(th)

def p33(th):
    return 15*pow(sin(th),3)

def assoc_legendre(m,l):
    if l==0 and m==0:
        return p00
    if l==1 and m==0:
        return p10
    if l==1 and m==1:
        return p11
    if l==2 and m==0:
        return p20
    if l==2 and m==1:
        return p21
    if l==2 and m==2:
        return p22
    if l==3 and m==0:
        return p30
    if l==3 and m==1:
        return p31
    if l==3 and m==2:
        return p32
    if l==3 and m==3:
        return p33

def assoc_laguerre(p,qmp):
    c = ((-1)**qmp)*fact(qmp+p)/fact(qmp)*special.genlaguerre(qmp,p,monic=True)
    return c

def angular_wave_func(m,l,theta,phi):
    if m>0:
        epsilon = (-1)**m
    else:
        epsilon = 1
    const = sqrt((2*l+1.0)/(4.0*pi) * float((fact(l-abs(m)))/float(fact(l+abs(m)))))
    
    z = complex(0,m*phi)
    
    ex = cmath.exp(z)
    
    f = assoc_legendre(m,l)
    
    Y = epsilon * const * ex * f(theta)
    
    w = round(Y.real,5)
    x= complex(0,round(Y.imag,5))
    Y = w+x
    return Y

def radial_wave_func(n,l,r):
    a=physical_constants["Bohr radius"][0]
    const = sqrt(((2.0/n)**3) * (float(fact(n-l-1))/float(2*n*(fact(n+l))**3))) #normalised to a^-3/2
    ex = exp(-r/(n*a)) *((2*r/(n*a))**l)
    p = 2*l+1
    qmp = n-l-1
    f = assoc_laguerre(p,qmp)
    laguerre_formula = f((2*r)/(n*a))
    result = const*ex*laguerre_formula
    return round(result,5)

def hydrogen_wave_func(n,l,m,r0a,Nx,Ny,Nz):
    a=physical_constants["Bohr radius"][0]
    x = linspace(-r0a,r0a,Nx)
    y = linspace(-r0a,r0a,Ny)
    z = linspace(-r0a,r0a,Nz)
    xx,yy,zz=meshgrid(x,y,z)
    vcartesian_to_spherical = vectorize(cartesian_to_spherical)
    (r,theta,phi) = vcartesian_to_spherical(xx,yy,zz)
    
    def test(r,theta,phi):
        if m==0:
            wave_func = radial_wave_func(n,l,(r*a))*angular_wave_func(m,l,theta,phi)
            density = (absolute(wave_func))**2
            return round(density,5)
        else:
            wave_func = 2*(radial_wave_func(n,l,(r*a)))*(angular_wave_func(m,l,theta,phi))
            wave_tot = wave_func + wave_func
            density = abs(wave_tot)
            mag_den = density**2
            return round(mag_den,5)
    
    myfunc = vectorize(test)
    mag = myfunc(r,theta,phi)
    return xx,yy,zz,mag