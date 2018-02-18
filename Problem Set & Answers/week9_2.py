"""
from libdw import sm

class SimpleAccount(sm.SM):
    def __init__(self, start_deposit):
        self.startState=start_deposit

    def getNextValues(self, state, inp):
        if inp<0 and state<100:
            next_state=state+inp-5
        else:
            next_state=state+inp
        output=next_state
        return next_state, output
"""

from libdw import sm
class SimpleAccount(sm.SM):
    def __init__(self,balance):
        self.startState=balance
    
    def getNextValues(self,state,inp):
        if state<100 and inp<0:
            nextState=state+inp-5
        else:
            nextState=state+inp
        return nextState,nextState
        
acct=SimpleAccount(110) 
acct.start() 
print acct.step(10) 
#120 
print acct.step(-25) 
#95 
print acct.step(-10) 
#80 
print acct.step (-5) 
#70 
print acct.step(20) 
#90 
print acct.step(20) 
#110
