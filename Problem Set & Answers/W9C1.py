from libdw import sm

class CM(sm.SM):
    startState=0
    def getNextValues(self,state,inp):
        if state==0 and inp==100:
            nextstate=0
            output=(0,'coke',0)
        elif state==0 and inp==50:
            nextstate=1
            output=(50,'--',0)
        elif  state==0 and inp==0:
            nextstate=0
            output=(0,'--',0)
        elif state==1 and inp==100:
            nextstate=0
            output=(0,'coke',50)
        elif state==1 and inp==50:
            nextstate=0
            output=(0,'coke',0)
        elif state==0 and inp==10:
            nextstate=0
            output=(0,'--',10)
        elif state==1 and inp==10:
            nextstate=0
            output=(0,'--',10)
        return nextstate,output
            
c=CM()        
c.start() 
c.step(50)                   
print c.step(50)
            
