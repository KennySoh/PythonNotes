from libdw import sm
class RingCounter(sm.SM):
    startState = '000'  # fix this

    def getNextValues(self, state, inp):
        if state=="000" and inp==0:
            nextState="001"
            output=nextState
            return nextState,output
        elif state=="001" and inp==0:
            nextState="010"
            output=nextState
            return nextState,output
        elif state=='010' and inp==0:
            nextState='011'
            output=nextState
            return nextState,output
        elif state=='011' and inp==0:
            nextState='100'
            output=nextState
            return nextState,output
        elif state=='100' and inp==0:
            nextState='101'
            output=nextState
            return nextState,output
        elif state=='101' and inp==0:
            nextState='110'
            output=nextState
            return nextState,output
        elif state=='110' and inp==0:
            nextState='111'
            output=nextState
            return nextState,output
        elif state=='111' and inp==0:
            nextState='000'
            output=nextState
            return nextState,output
        elif inp==1:
            nextState='000'
            output=nextState
            return nextState,output
print 'test 1'
r=RingCounter()
print r.transduce([0,0,0,0,0,0,0,0,0])
print 'test 2'
r=RingCounter()
print r.transduce([0,0,0,1,0,0,0,0,0])
print 'test 3'
r=RingCounter()
print r.transduce([0,0,0,1,0,0,1,0,0])
            
    