def countNumOpenLocker(K):
        K_list=[]
        for i in range(0,K):
            K_list.append("o")
        for j in range (1,K+1):
            #if j==1:
                #print K_list
            if j==2:
                for j_inner in range(1,K,2):
                    K_list[j_inner]="c"
                #print K_list
            if j==3:
                for j_inner in range(2,K,3):
                    K_list[j_inner]=toggle(K_list[j_inner])
                #print K_list
            if j>=4:
                for j_inner in range(j-1,K,j):
                    K_list[j_inner]=toggle(K_list[j_inner])
                #print K_list
        output=0
        for t in K_list:
            if t=="o":
                output+=1
        #print K_list
        print output
        return output
                

def toggle(inp):
    if inp=="o":
        return "c"
    if inp=="c":
        return "o"

#countNumOpenLocker(6)
countNumOpenLocker(2000) #returns 44
countNumOpenLocker(10) #returns 3
countNumOpenLocker(20) #returns 4