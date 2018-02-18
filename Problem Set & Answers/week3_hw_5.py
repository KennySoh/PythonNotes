import math
def approx_ode(h,t0,y0,tn):
    x=tn/h
    counter=1
    while counter<=int(x):
        y0=y0+h*f(t0,y0)
        t0=h+t0
        #print(y0,counter,x,t0)
        counter=counter+1
    return round(y0,3)

def f(t, y):
    return 3.0+math.exp(-t)-0.5*y

print approx_ode(0.1,0,1,3.0)
print approx_ode(0.1,0,1,4.0)
print approx_ode(0.1,0,1,5.0)
print approx_ode(0.1,0,1,0.0)