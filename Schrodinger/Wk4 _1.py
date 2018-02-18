import math as m

import numpy as np 
from Wk3_2 import assoc_legendre

def factorial(n):
    if n == 0:
        return 1
    else:
        return m.factorial(n)
        
def angular_wave_func(m_1,l,theta,phi):
    if m_1>0:
        e=(-1.0)**m_1
    if m_1<=0:
        e=1.0
    
    soln_1=e*((2*l+1.0)*factorial(l-abs(m_1))/((4.0*m.pi)*(factorial(l+abs(m_1)))))**(0.5)
    soln_2=m.cos(m_1*phi)+m.sin(m_1*phi)*1.0j         #exp(i*m*phi) eluer formula
    
    pfunc=assoc_legendre(m_1,l)  #return a funciton (theta)
    soln_3=pfunc(theta)
    soln_total=soln_1*soln_2*soln_3
    soln_total=np.round(soln_total,5)
    return soln_total # <<<m,l,phi   qns 2e
                # complex number 5 dec for both real and imaginary

        
print "angular_wave_func (0,0,0,0)"
ans= angular_wave_func (0,0,0,0)
print ans
print "angular_wave_func (0,1,c.pi ,0)"
ans= angular_wave_func (0,1,m.pi ,0)
print ans
print "angular_wave_func (1,1,c.pi/2,c.pi)"
ans= angular_wave_func (1,1,m.pi/2,m.pi)
print ans
print "angular_wave_func (0,2,c.pi ,0)"
ans= angular_wave_func (0,2,m.pi ,0)
print ans


 
 
 
 