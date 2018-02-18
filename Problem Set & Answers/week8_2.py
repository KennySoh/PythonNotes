class Celsius(object):
    def __init__(self,temperature=0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return (self.temperature *1.8)+32
    
    def get_temperature(self):
        print "get temperature"
        return self._temperature
    
    def set_temperature(self,value):
        
        if value<-273:
            self._temperature=-273
        else:
            self._temperature=value
    temperature = property(get_temperature,set_temperature) #***
    
c=Celsius()
c.temperature=-999999999
print c.temperature
