def reverse(s):
    j=[]
    for i in range(0,len(s)):
        j.append(s[len(s)-i-1])
    z="".join(j)
    return z
    
    
    
print reverse("crap")