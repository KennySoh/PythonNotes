import math
#return only the derivative value without rounding
#your return value is a float, which is the approximate value of the derivative
#Tutor will compute the approximate error based on your return value

class Diff(object):
    def __init__(self,f,h=1E-4):
        self.f=f
        self.h=h
    def __call__(self,x):
        return (self.f(x+self.h)-self.f(x))/self.h
"""
def f(x): 
    return 0.25*x**4
df = Diff(f) # make function -like object df
        # df(x) computes the derivative of f(x) approximately:
for x in (1, 5, 10): 
    df_value = df(x) # approx value of derivative of f at point x 
    exact = x**3 # exact value of derivative 
    print "f’(%d)=%g (error=%.2E)"%(x, df_value , exact-df_value)
"""  
def g(x): 
    return math.log(x)
df = Diff(g,0.1) # make function -like object df
        # df(x) computes the derivative of f(x) approximately:
exact=0.1
df_value = df(10) # approx value of derivative of f at point x 
print (df_value,exact-df_value)
""" 
import math

def f(x):
    return math.log(x)

df = Diff(f,1)

df_value = df(10)
print df_value
exact = 0.1
print exact-df_value
"""