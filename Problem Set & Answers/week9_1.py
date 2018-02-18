class CM(sm.SM):
    startState = 0
    def getNextValues(self,state_1, inp):
        if state_1 == 0 and inp == 100:
            nextState = 0
            output=(0,'coke',0)

        elif state_1 == 1 and inp ==100:
            nextState = 0
            output = (0, 'coke', 50)
        elif state_1 == 0 and inp == 50:
            nextState = 1
            output=(50,'--',0)
        elif state_1 == 1 and inp==50:
            nextState = 0
            output = (0,'coke',0)
        else:
            nextState = state_1
            output = (0,'--',inp)
        return nextState,output
#amount in , coke ?, change
c=CM()
c.start()
print c.step(50)
#(50, ’--’, 0)
print c.step(50)
#(0, ’coke’, 0)
print c.step(100)
#(0, ’coke’, 0)
print c.step(10)
#(0, ’--’, 10)
print c.step(50)
#(50, ’--’, 0)
print c.step(100)
#(0, ’coke’, 50)
print c.step(10)
#(0, ’--’, 10)
