import sys as sys
def max_list(inp):
#inp= [[1,23],[1,23,3]]
    ls=[]  
    for x in range(0,len(inp)):
        sum=-sys.float_info.max
        for y in range(0,len(inp[x])):
            if inp[x][y]>sum:
                sum=inp[x][y]
        ls.append(sum)
    return ls

inp = [[1 ,2 ,3] ,[4 ,5]]
print max_list ( inp )
#[3, 5]
inp = [[1 ,2 ,3] ,[4 ,5] ,[32 ,3 ,4]]
print max_list ( inp )
#[3, 5, 32]
inp = [[3 ,4 ,5 ,2] ,[1 ,7] ,[8 ,0 , -1] ,[2]]
print max_list ( inp )
#[5, 7, 8, 2]
inp = [[100] ,[1 ,7] ,[ -8 , -2 , -1] ,[2]]
print max_list ( inp )
#[100 , 7, -1, 2]
inp = [[3 ,4 ,5 ,2]]
print max_list(inp)