class Polynomial(object):
    def __init__(self,coeff):
        self.coeff=coeff
        #print self.coeff
    def __add__(self,other):
        ls=[]
        if len(self.coeff)>=len(other.coeff):
            for i,val in enumerate(self.coeff):
                if len(other.coeff)>i:
                    ls_new=val+other.coeff[i]
                else:
                    ls_new=val
                ls.append(ls_new)
        else:
            for i,val in enumerate(other.coeff):
                if len(self.coeff)>i:
                    ls_new=val+self.coeff[i]
                else:
                    ls_new=val

                ls.append(ls_new)
        return Polynomial(ls)
        
    def __sub__(self,other):
        ls=[]
        if len(self.coeff)>=len(other.coeff):
            for i,val in enumerate(self.coeff):
                if len(other.coeff)>i:
                    ls_new=val-other.coeff[i]
                else:
                    ls_new=val
                ls.append(ls_new)
        else:
            for i,val in enumerate(other.coeff):
                if len(self.coeff)>i:
                    ls_new=-val+self.coeff[i]
                else:
                    ls_new=-val

                ls.append(ls_new)
        return Polynomial(ls)
    def __call__(self,x):
        total=0
        for i,val in enumerate(self.coeff):
            total+=val*x**i
        return total
    def __mul__(self,other):
        total={}
        for i,val_i in enumerate(self.coeff):
            for j,val_j in enumerate(other.coeff):
               #print val_i,val_j
                #print total.keys()
                if i+j not in total.keys():
                    total[i+j]=val_i*val_j
                else:
                    
                    total[i+j]+=val_i*val_j
        #print total
        ls_1=[]
        final=[]
        for dict_keys in total:
            ls_1.append(dict_keys)
        
        ls_1.sort()
        for dict_counter in ls_1:
            final.append(total[dict_counter])
        return Polynomial(final)
    def derivative(self):
        ls=[]
        for i,value in enumerate(self.coeff):
            if i==0:
                pass
            else:
                ls.append(i*value)
        return Polynomial(ls)
    def differentiate(self):
        ls=[]
        for i,value in enumerate(self.coeff):
            if i==0:
                pass
            else:
                ls.append(i*value)
        self.coeff=ls
        
p10=Polynomial([1, 3, 5, 7, 9])
p10.differentiate()

p1=Polynomial([1,-1])
p2=Polynomial([0,1,0,0,-6,-1])
#p3 = p1 + p2
#print p3.coeff
#[1, 0, 0, 0, -6, -1]
#print p2(1)
p4 = p1*p2
print p4.coeff
#[0, 1, -1, 0, -6, 5, 1]
p5=p2.derivative()
print p5.coeff
#[1, 0, 0, -24, -5]
p = Polynomial([1 , 2, 3])
q = Polynomial([2 , 3])
r=p-q
print r. coeff
#[-1, -1, 3]
r=q-p
print r. coeff
#[1, 1, -3]