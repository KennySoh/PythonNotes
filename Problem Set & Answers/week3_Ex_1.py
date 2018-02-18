def may_ignore(x):
    Type_1=type(x)
    if Type_1==int:
        return x+1
    else:
        return None

print may_ignore(1)
print may_ignore(1.0)
print may_ignore(1+2j)
print may_ignore("Hello")