from libdw import sm
class FirstWordSM(sm.SM):
    startState = 0  # fix this

    def getNextValues(self, state, inp):
        if state==0 and inp== " ":
            nextState=0
            output=None
            return nextState,output
        elif state==0 and inp=="\n":
            nextState=0
            output=None
            return nextState,output
        
        elif state==0 and inp!= " "and inp!="\n":
            nextState=1
            output=inp
            return nextState,output
        elif state==1 and inp!= " ":
            nextState=1
            output=inp
            return nextState,output
        elif state==1 and inp== " ":
            nextState=2
            output=None
            return nextState,output
        elif state==2 and inp!= "\n":
            nextState=2
            output=None
            return nextState,output
        elif state==2 and inp== "\n":
            nextState=0
            output=None
            return nextState,output
str = 'def f(x): # comment\n   return 1'
m = FirstWordSM()
print m.transduce(str)
#['d', 'e', 'f', 
#None, None, None, None, None, None, None, None, None, None,
#None, None, None, None, None, None, None, None, None, None, 
#'r', 'e', 't', 'u', 'r', 'n', 
#None, None]


"""
0->1, return inp if inp not" "
0->0, return None if inp==" "
1->1, return inp if not inp=" "
1->2, return None if inp==" "
2->2,return None if not inp="\n"
2->0, return None if inp="\n"



2->2, return None if inp=" "
2->3, return inp if not inp=" "
3->3. return inp if not inp=" "
3->4  return None if inp=" "
"""