
# coding: utf-8

# 1.

# In[ ]:

class Coordinate(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def magnituge(self):
        return ((self.x**2)+(self.y**2))**0.5
    
    def translate(self,dx,dy):
        self.x = self.x+dx
        self.y = self.y+dy
    
    def __eq__(self,other):
        if (self.x==other.x) and (self.y==other.y):
            return True
        else:
            return False



# 2.

# In[77]:

class Celsius(object):
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print "get temp"
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            print "set"
            self._temperature = -273
        else:
            print "set"
            self._temperature = value

    temperature = property(get_temperature,set_temperature)
    
c = Celsius()
print (c.temperature)
c.temperature = 32
print (c.to_fahrenheit())
c.temperature = -300
print (c.temperature)


# 3.

# In[3]:

import time 

class StopWatch:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = -1
    def start(self):
        self.start_time = time.time()
        self.end_time = -1
    def stop(self):
        self.end_time = time.time()
    def elapsed_time(self):
        if self.end_time == -1:
            return None
        else:
            return round(self.end_time-self.start_time,1)
    
sw = StopWatch()
time.sleep(0.1)
sw.stop()
print sw.elapsed_time()
sw.start()
time.sleep(0.2)
print sw.elapsed_time()
sw.stop()
print sw.elapsed_time()


# 4.

# In[156]:

import numpy as np

class Line():
    def __init__(self,c_0,c_1):
        self.c_0 = c_0
        self.c_1 = c_1
    def __call__(self,x):
        return float(self.c_0+self.c_1*x)
    
    def table(self,L,R,n):
        xx=np.linspace(L,R,n)
        for num in xx:
            print "%-10.2f%-10.2f"%(num,self(num))
                                    
line=Line(3,4)
print line(2)

print line.table(1,5,15)


# In[12]:

import numpy as np

class Line():
    def __init__(self,c_0,c_1):
        self.c_0 = c_0
        self.c_1 = c_1
    def __call__(self,x):
        return float(self.c_0+self.c_1*x)
    
    def table(self,L,R,n):
        if L==R:
            n=1
        xx=np.linspace(L,R,n)
        retval = ""
        for num in xx:
            retval = retval + "%10.2f%10.2f\n"%(num,self(num))
        if retval == "":
            return "Error in printing table"
        else:
            return retval
line=Line(3,4)
print line(2)
    
print line.table(1,1,15)


# 1.

# In[178]:

class Time(object):
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def get_time(self):
        return (self.hours*3600 + self.minutes*60 + self.seconds)

    def set_time(self,value):
        self.hours = (value%86400)/3600
        self.minutes = (value%3600)/60
        self.seconds = (value%60)
    
    elapsed_time = property(get_time,set_time)
        
    def __str__(self):
        return "Time: {}:{}:{}".format(self.hours,self.minutes,self.seconds)

t = Time(10,19,10)
print t.elapsed_time
t.elapsed_time = 5555
print t.elapsed_time
print t


# 2.

# In[27]:

class Account:
    def __init__(self,owner,account_number,amount):
        self.owner = owner
        self.account_number = account_number
        self.amount = amount
    
    def deposit(self,amount):
        self.amount = self.amount+amount
        
    def withdraw(self,amount):
        self.amount = self.amount-amount
    
    def __str__(self):
        return "%s, %s, balance: %d"%(self.owner,self.account_number,self.amount)

a1 = Account ("John Olsson","19371554951",20000)
a2 = Account ("Liz Olsson","19371564761",20000)
a1.deposit (1000)
a1.withdraw (4000)
a2.withdraw (10500)
a1.withdraw (3500)
print a1

print a2

        


# 3.

# In[20]:

class Diff(object):
    def __init__(self,f,h=10**-4):
        self.f = f
        self.h = h
    
    def __call__(self,x):
        return(self.f(x+self.h)-self.f(x))/(self.h)

def f(x):
    return 0.25*x**4

df = Diff(f,1)

for x in (1,5,10):
    df_value = df(x)
    exact = x**3
    print "f’(%d)= %g (error =%.2E)" % (x , df_value , exact - df_value )
        


# In[24]:

import math

def f(x):
    return math.log(x)

df = Diff(f,1)

df_value = df(10)
print df_value
exact = 0.1
print exact-df_value


# In[81]:

class Polynomial:
    def __init__(self,coeff):
        self.coeff = coeff[:]
    
    def __call__(self,x):
        c = 0
        for i,val in enumerate(self.coeff):
            c += val*(x**i)
        return c
        
    
    def __add__(self,other):
        tempselfcoeff = self.coeff[:]
        tempothercoeff = other.coeff[:]
        if len(self.coeff)<len(other.coeff):
            for i in range(len(other.coeff)-len(self.coeff)):
                tempselfcoeff.append(0)
        else:
            for i in range(len(self.coeff)-len(other.coeff)):
                tempothercoeff.append(0)
                
        newcoeff = []
        for i,val in enumerate(tempselfcoeff):
            
            newcoeff.append(val+tempothercoeff[i])
        return Polynomial(newcoeff)
    
    def __sub__(self,other):
        tempselfcoeff = self.coeff[:]
        tempothercoeff = other.coeff[:]
        if len(self.coeff)<len(other.coeff):
            for i in range(len(other.coeff)-len(self.coeff)):
                tempselfcoeff.append(0)
        else:
            for i in range(len(self.coeff)-len(other.coeff)):
                tempothercoeff.append(0)
                
        newcoeff = []
        for i,val in enumerate(tempselfcoeff):
            
            newcoeff.append(val-tempothercoeff[i])
        return Polynomial(newcoeff)
    
    def __mul__(self,other):
        tempselfcoeff = self.coeff[:]
        tempothercoeff = other.coeff[:]
        newcoeff=[0 for i in range(len(self.coeff)+len(other.coeff)-1)]
        
        if len(self.coeff)<len(other.coeff):
            for i in range(len(other.coeff)-len(self.coeff)):
                tempselfcoeff.append(0)
        else:
            for i in range(len(self.coeff)-len(other.coeff)):
                tempothercoeff.append(0)
        
        
        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                newcoeff[(i+j)] += tempselfcoeff[i]*tempothercoeff[j]
        return Polynomial(newcoeff)
    
    def differentiate(self):
        for i,val in enumerate(self.coeff):
            try:
                self.coeff[i] = self.coeff[i+1]*(i+1)
            except IndexError:
                self.coeff.pop(i)
    def derivative(self):
        newcoeff = [0 for i in range(len(self.coeff)-1)]
        for i,val in enumerate(self.coeff):
            try:
                newcoeff[i] = self.coeff[i+1]*(i+1)
            except IndexError:
                pass
        return Polynomial(newcoeff)
    
    
p1 = Polynomial([1,-1])
p2 = Polynomial([0,1,0,0,-6,-1])
p3 = p1+p2

print p3.coeff

p4 = p1*p2
p3 = p1*p2
print p4.coeff

p4.differentiate()
print p4.coeff

p5 = p3.derivative()
print p5.coeff

print p2(3)


# In[35]:

newcoeff=[0 for i in range(10)]
print newcoeff


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



