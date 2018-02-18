
from libdw import sm
class Elevator(sm.SM):
    def __init__(self):
        self.startState='First'
    
    def getNextValues(self,state,inp):
        if state=="First" and inp=="Up":
            nextState="Second"
            output=nextState
            return nextState,output
        if state=="Second" and inp=="Up":
            nextState="Third"
            output=nextState
            return nextState,output
        if state=="Third" and inp=="Up":
            nextState="Third"
            output=nextState
            return nextState,output
        if state=="First" and inp=="Down":
            nextState="First"
            output=nextState
            return nextState,output
        if state=="Second" and inp=="Down":
            nextState="First"
            output=nextState
            return nextState,output
        if state=="Third" and inp=="Down":
            nextState="Second"
            output=nextState
            return nextState,output
            
e = Elevator()
print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up'])