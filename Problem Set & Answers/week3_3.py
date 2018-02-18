def list_sum(a):
    if a==[]:
        return "0.0"
    else:
        n=0
        x=0.0
        while n<len(a):
            x=a[n]+x  
            n=n+1
        x="%.1f"%x    
        return x

print (" Test case 1: [4.25 ,5.0 ,10.75] ")
ans= list_sum ([4.25 ,5.0 ,10.75])
print ans
print (" Test case 2: [5.0] ")
ans= list_sum ([5.0])
print ans
print (" Test case 3: []")
ans= list_sum ([])
print ans