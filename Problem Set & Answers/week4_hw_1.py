def f_to_c(F):
    C=(F-32.0)/1.8
    return round(C,1)

def f_to_c_approx(F):
    C=(F-30.0)/2.0
    return round(C,1)

def get_conversion_table():
    ls_table=[]
    for F in range (0,110,10):
        ls=[F,f_to_c(F),f_to_c_approx(F)]
        ls_table.append(ls)
    #return ls_table
#def conversion(ls_table):
    x_outer=[]
    for i in range(0,3):
        #print i
        x=[]
        for j in range(0,len(ls_table)):
            #print ls[j][i]
            x.append(ls_table[j][i])
        x_outer.append(x)
    return x_outer
table=get_conversion_table()
print conversion(table)
#(122 degrees Fahrenheit - 32)  ÷ 1.8 = 50 degrees Celsius
