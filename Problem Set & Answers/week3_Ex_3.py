import math
def approx_pi(n):
    y=0.0
    for k in range(0,n+1):
        y=((math.factorial(4*k))*(1103.0+26390.0*k))/((math.factorial(k))**4.0*396.0**(4.0*k))+y
    x=(2.0*(2.0)**(1/2.0)/9801.0)*y
    pi=1.0/x
    return pi
    
print approx_pi(2)