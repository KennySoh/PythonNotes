def most_frequent(numList):
    dict1={}
    ls=[]
    y=0
    for x in range(0,len(numList)):
        if numList[x] not in dict1.keys():
            dict1[numList[x]]=1
        else:
            dict1[numList[x]]+=1
    for x in dict1.keys():
        if dict1[x]>y:
            y=dict1[x]
    for x in dict1.keys():
        if dict1[x]==y:
            ls.append(x)
        
    return ls

print most_frequent([1,2,3,4,1])