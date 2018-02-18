class CommentsSM(sm.SM):
    startState = "notComment"  # fix this

    def getNextValues(self, state, inp):
        if state=="notComment" and inp=="#":
            nextState="Comment"
            output=inp
            return nextState,output
        elif state=="notComment" and inp !="#": 
            nextState="notComment"
            output=None
            return nextState,output
        elif state=="Comment" and inp=="\n":
            nextState="notComment"
            output=None
            return nextState,output
        elif state=="Comment" and inp!="\n":
            nextState="Comment"
            output=inp
            return nextState,output
            
    
    
    
str = 'def f(x): # comment\n   return 1'
m = CommentsSM()
print m.transduce(str)
#[None, None, None, None, None, None, None, None, None, None, 
#'#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', 
#None, None, None, None, None, None, None, None, None, None, None, None]


