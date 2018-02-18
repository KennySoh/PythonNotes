#"""
import time 
class StopWatch(object):
    def __init__(self,astart1=time.time(),end1=-1):
        #print time.time()
        self.start1=astart1
        self.end1=end1
    def stop(self):
        self.end1 = time.time()
    def elapsed_time(self):
        #print self.end1
        #print self.start1
        self.time=round((self.end1-self.start1)*1000,1)
        if self.end1 <= 0:
            return None
            
        return self.time
    def start(self):
        self.start1 = time.time()
        self.end1= -1
        

sw = StopWatch()
time.sleep(0.1)
sw.stop()
print sw.elapsed_time()
sw.start()
time.sleep(0.2)
print sw.elapsed_time()
sw.stop()
print sw.elapsed_time()







