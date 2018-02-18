def longest_common_prefix(s1,s2):
    if len(s1)<len(s2):
        s=s1
    else:
        s=s2
    j=[]
    z=''
    for i in range(0,len(s)):
        if s1[i]==s2[i]:
            j.append(s1[i])
        else:
            z=''.join(j)
            return z
    z=''.join(j)        
    return z
            
            
print "longest_common_prefix(‘distance’,‘disinfection ’)" 
ans=longest_common_prefix('distance','disinfection') 
print ans
print "longest_common_prefix(‘testing’,‘technical ’)" 
ans=longest_common_prefix('testing','technical') 
print ans
print "longest_common_prefix(‘drinking’,‘drinker ’)" 
ans=longest_common_prefix('drinking','drinker') 
print ans
print "longest_common_prefix(‘rosses’,‘crosses ’)" 
ans=longest_common_prefix('rosses','crosses') 
print ans
print "longest_common_prefix(‘distancetion ’,‘distance ’)" 
ans=longest_common_prefix('distancetion','distance') 
print ans
