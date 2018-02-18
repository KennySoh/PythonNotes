import math
def is_prime(n):
    x=2.0
    prime=True
    if n<=1:
        prime=False
    while x<=math.sqrt(n):
        if n%x==0:
            prime=False
        x=x+1
    return prime
    
print " is_prime (2)"
ans= is_prime (2)
print ans
print " is_prime (3)"
ans= is_prime (3)
print ans
print " is_prime (7)"
ans= is_prime (7)
print ans
print " is_prime (9)"
ans= is_prime (9)
print ans
print " is_prime (21) "
ans= is_prime (21)
print ans