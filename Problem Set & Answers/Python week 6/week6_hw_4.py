def get_fundamental_constants(f):
    ls=[]
    dict_1={}    
    lines=f.readlines()
    #print lines
    for i in range(2,len(lines)):
        temp_1=lines[i].strip() #get rids of \n
        temp=temp_1.split()
        #print temp[]
        for i in range(0,len(temp[1])):
            if temp[1][i]=="e":
                #print float(temp[1][0:i]),(int(temp[1][i+1:len(temp[1])]))
                j=float(temp[1][0:i])*10**(int(temp[1][i+1:len(temp[1])]))
            else:
                j=float(temp[1])
        dict_1[temp[0]]=j
        ls.append(temp)
    #print ls
    return dict_1
    


f=open('constants.txt','r')
print get_fundamental_constants(f)

