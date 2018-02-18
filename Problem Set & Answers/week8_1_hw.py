class Time(object):
    def __init__(self,hrs,mins,seconds):
        self.hrs=hrs
        self.mins=mins
        self.seconds=seconds
    
    def get_time(self):
        return self.hrs*60*60+self.mins*60+self.seconds
    
    def set_time(self,value):
        self.seconds=value%60
        self.mins=(value//(60))%60
        self.hrs=(value//(60*60))%24
    elapsed_time=property(get_time,set_time)
    def __str__(self):
        return "Time:%3d:%d:%d"%(self.hrs,self.mins,self.seconds)
t=Time(10 , 19, 10)
print t.elapsed_time
print t.seconds,t.mins,t.hrs
t.elapsed_time =555550
print t.seconds,t.mins,t.hrs
#print t.elapsed_time
print t

"""
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
t.elapsed_time = 55550
print t.elapsed_time
print t
"""