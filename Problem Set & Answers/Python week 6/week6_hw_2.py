def uncompressed(s):
    final=""
    for i in range(0,len(s),2):
        number=int(s[i])
        final+=(s[i+1]*number)
        
    return final
    
print uncompressed("2a5b1c")
