
def maxOccurrences(inp):
    dict_1={}
    inp=inp.split()
    for i in inp:
        if i in dict_1.keys():
            dict_1[i]+=1
        else:
            dict_1[i]=1
    values=[]
    maxoccurence=0
    for j in dict_1.keys():
        if dict_1[j]>maxoccurence:
            maxoccurence=dict_1[j]
    for z in dict_1.keys():
        if dict_1[z]==maxoccurence:
            values.append(int(z))
            values.sort()
    return (values,maxoccurence)
    
print 'test 1'
inp='2 3 40 3 5 4 -3 3 3 2 0'
print maxOccurrences(inp)
print 'test 2'
inp='9 30 3 9 3 2 4'
print maxOccurrences(inp)