def get_base_counts(DNA):
    x=0
    count=[0,0,0,0,0]
    while x<len(DNA):
        if DNA[x]=="A":
            count[0]+=1
        if DNA[x]=="C":
            count[1]+=1
        if DNA[x]=="G":
            count[2]+=1 
        if DNA[x]=="T":
            count[3]+=1       
        x+=1
    count[4]=count[0]+count[1]+count[2]+count[3]
    
    DNA_dict={}
    if count[0]!=0:
        DNA_dict['A']=count[0]
    if count[1]!=0:
        DNA_dict['C']=count[1]
    if count[2]!=0:
        DNA_dict['G']=count[2]
    if count[3]!=0:
        DNA_dict['T']=count[3]
   
    if count[4]<len(DNA):
        return "The input DNA string is invalid"
    else:
        return DNA_dict
        
    
    


        
#Test case 1
print get_base_counts("AACCGT")
#Output: f`A`: 2, `C': 2, `G`: 1, `T': 1g
#Test case 2
print get_base_counts('AAB')
#Output: `The input DNA string is invalid'
#Test case 3
print get_base_counts('AaCaGT')
#Output: `The input DNA string is invalid'