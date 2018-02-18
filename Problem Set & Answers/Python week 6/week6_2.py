def check_password(password):
    if len(password)>=8:
        count=0
        digit=0
        for i in range(0,len(password)):
            if password[i].isdigit():
                digit+=1
                count+=1
            elif password[i].isalpha():
                count+=1
        if count==len(password):
            if digit>=2:
                return True
    return False


print "check_password(‘test ’)"
ans=check_password("test") 
print ans
print "check_password(‘testtest’)" 
ans=check_password("testtest ") 
print ans
print "check_password(‘testt22’)" 
ans=check_password("testt22") 
print ans
print "check_password(‘testte22 ’)" 
ans=check_password('testte22') 
print ans
