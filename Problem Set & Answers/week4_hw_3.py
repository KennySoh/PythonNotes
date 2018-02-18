def multiplication_table(N):
    ls=[]
    if N<1:
        return None
    for i in range(1,N+1):
        ls.append([])
        for j in range (1,N+1):
            ls[i-1].append(i*j)
    
    return ls
    
print multiplication_table(7)
    
print multiplication_table(1)
print multiplication_table(0)
print multiplication_table(2)
print multiplication_table(-1)