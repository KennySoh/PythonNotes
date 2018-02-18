import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def throw_dice(n, nExp):
    #(1/6)**(n-2)*(5/6)**2+(1/6)**(n-1)*(5/6)*1+(1/6)**n
    prob=1.0-(5.0/6.0)**n
    return prob
print throw_dice(2,1)
