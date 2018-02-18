import math
def simpsons_rule(f, n, a, b):
    a=float(a)
    b=float(b)
    h=(b-a)/n

    x_0=a
    x_n=b
    sum_f_x_2j=0.0
    sum_f_x_2j_1=0.0
    
    j=1
    while j<=(n/2-1):
        sum_f_x_2j=sum_f_x_2j+f(a+2*j*h)
        j=j+1
    j=1
    while j<=n/2:
        sum_f_x_2j_1=sum_f_x_2j_1+f(a+(2.0*j-1)*h)
        print sum_f_x_2j_1,j
        j=j+1
        

    total=(h/3.0)*(f(x_0)+2.0*sum_f_x_2j+4.0*sum_f_x_2j_1+f(x_n))
    print sum_f_x_2j,sum_f_x_2j_1
    
    #return round(total,2)
    return total
    
    
def f1(x):
    return x**2

def f2(x):
    return math.sin(x)

def f3(x):
    return math.exp(-x)

print simpsons_rule(f1,1000,1,3)
#print simpsons_rule(f2,1000,0,math.pi)
#print simpsons_rule(f3,1000,-1,1)