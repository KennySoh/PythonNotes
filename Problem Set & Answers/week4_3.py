def find_average(ls):
    Average_ls=[]
    counter=0
    Last=[0.0,0.0]
    while counter<len(ls):
        if type(ls[counter])==list:
            #print ls[counter]
            counter_1=0
            Total=0.0
            while counter_1<len(ls[counter]):
                Total=ls[counter][counter_1]+Total
                counter_1=counter_1+1
            t=len(ls[counter])
            #print Total,t
            if t==0:
                Average=0.0
                Last[0]=Total+Last[0]
                
            else:
                Average=Total/float(t)
                Last[0]=Total+Last[0]
        else:        
            Average=ls[counter]
            Last[0]=Average+Last[0]
        
        Last[1]= len(ls[counter])+Last[1]    
        #print Average
        Average_ls.append(Average)
        counter=counter+1
    last=Last[0]/Last[1]
    ls_final=(Average_ls,last)
    return ls_final
    
ans= find_average ([[3 ,4] ,[5 ,6 ,7] ,[ -1 ,2 ,8]])
print ans
#([3.5 , 6.0 , 3.0] , 4.25)
ans= find_average ([[13.13 ,1.1 ,1.1] ,[] ,[1 ,1 ,0.67]])
print ans
#([5.11 , 0.0 , 0.89] , 3.0)
ans= find_average ([[3.6] ,[1 ,2 ,3] ,[1 ,1 ,1]])
print ans
#([3.6 , 2.0 , 1.0] , 1.8)