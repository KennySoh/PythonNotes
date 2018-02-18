def get_even_list(ls):
    n=0
    even_ls=[]
    while n<len(ls):
        if ls[n]%2==0:
            even_ls.append(ls[n])
        n=n+1
    return even_ls
    
print " get_even_list ([1 ,2 ,3 ,4 ,5])"
ans= get_even_list ([1 ,2 ,3 ,4 ,5])
print ans
print " get_even_list ([11 ,22 ,33 ,44 ,55]) "
ans= get_even_list ([11 ,22 ,33 ,44 ,55])
print ans
print " get_even_list ([10 ,20 ,30 ,40 ,50]) "
ans= get_even_list ([10 ,20 ,30 ,40 ,50])
print ans
print " get_even_list ([11 ,21 ,31 ,41 ,51]) "
ans= get_even_list ([11 ,21 ,31 ,41 ,51])
print ans