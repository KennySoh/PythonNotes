def transpose_matrix(matrix):
    transpose_ls=[]
    x=0
    while x<len(matrix[0]):#m
        g=0
        transpose_innerls=[]
        while g<len(matrix):#n
            transpose_innerls.append(matrix[g][x])
            g+=1
        transpose_ls.append(transpose_innerls)
        x+=1
    return transpose_ls