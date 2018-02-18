def my_reverse(list1):
    num_list_2=[]
    n=0
    while n<len(list1):
        num_list_2.append(list1[len(list1)-n-1])
        n=n+1
    return num_list_2

print my_reverse([1,2,3])