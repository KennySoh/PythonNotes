def is_palindrome(num):
    num_list_1=list(str(num))
    num_list_2=[]
    n=0
    while n<len(num_list_1):
        num_list_2.append(num_list_1[len(num_list_1)-n-1])
        n=n+1
    if num_list_1==num_list_2:
        return True
    else:
        return False
print (" Test case 1: 1")
ans= is_palindrome (1)
print ans
print (" Test case 2: 22")
ans= is_palindrome (22)
print ans
print (" Test case 3: 12321 ")
ans= is_palindrome (12321)
print ans
print (" Test case 4: 441232144 ")
ans= is_palindrome (441232144)
print ans
print (" Test case 5: 441231144 ")
ans= is_palindrome (441231144)
print ans
print (" Test case 6: 144")
ans= is_palindrome (144)
print ans
print (" Test case 7: 12")
ans= is_palindrome (12)
print ans