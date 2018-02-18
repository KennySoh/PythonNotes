def process_scores(f):
    scores=f.readlines()
    #print scores
    x=0.0
    for i in range(0,len(scores)):
        temp=scores[i].strip()
        #print temp
        x+=float(temp)
        #print x
    average=x/len(scores)
    return x,average



f=open('scores.txt','r')
print process_scores(f)