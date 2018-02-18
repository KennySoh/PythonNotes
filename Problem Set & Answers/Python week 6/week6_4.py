import sys
class Coordinate:
    x=0
    y=0

def get_maxmin_mag(f):
    Max=-sys.float_info.max
    Min=sys.float_info.max
    lines = f.readlines()
    #print lines
    for i in range(0,len(lines)):
        temp = lines[i].strip()
        #print temp
        x,y=temp.split()
        #print x,y
        x=float(x)
        y=float(y)
        mag=((x)**2+(y)**2)**0.5
        if Max<mag:
            Max=mag
            Maxx=x
            Maxy=y
        if Min>mag:
            Min=mag
            Minx=x
            Miny=y
    pmax= Coordinate()
    pmax.x=Maxx
    pmax.y=Maxy
    pmin= Coordinate()
    pmin.x=Minx
    pmin.y=Miny
    return pmax, pmin
    
f=open('xy.dat','r') 
pmax,pmin=get_maxmin_mag(f)
print 'max: (%f, %f)'%(pmax.x,pmax.y) 
print 'min: (%f, %f)'%(pmin.x,pmin.y)
