import sys

def minmax_in_list(ls):
    if ls==[]:
        return (None,None)
    else:
        n=0
        Max=-sys.maxint-1
        Min=sys.maxint
        
        while n<len(ls):
            
            if ls[n]>Max:
                Max=ls[n]
            if ls[n]<Min:
                Min=ls[n]
            n=n+1
        return (Min,Max)            
        
        
        
        
        
        
print (" Test case 1: [1 ,2 ,3 ,4 ,5]")
ans= minmax_in_list ([1 ,2 ,3 ,4 ,5])
print ans
print (" Test case 2: [1 ,1 ,3 ,0]")
ans= minmax_in_list ([1 ,1 ,3 ,0])
print ans
print (" Test case 3: [3 ,2 ,1]")
ans= minmax_in_list ([3 ,2 ,1])
print ans
print (" Test case 4: [0 ,10]")
ans= minmax_in_list ([0 ,10])
print ans
print (" Test case 5: [1]")
ans= minmax_in_list ([1])
print ans
print (" Test case 6: []")
ans= minmax_in_list ([])
print ans
print (" Test case 7: [1 ,1 ,1 ,1 ,1]")
ans= minmax_in_list ([1 ,1 ,1 ,1 ,1])
print ans