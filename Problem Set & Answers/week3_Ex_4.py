from fractions import Fraction
def gcd(a,b):
    x=Fraction(a,b)
    gcd=b/x.denominator
    return gcd

    
print gcd(1,2)
