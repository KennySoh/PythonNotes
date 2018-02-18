def binary_to_decimal(binaryStr):
    count=0
    s=0
    for i in range(0,len(binaryStr)):
        if int(binaryStr[len(binaryStr)-1-i])==1:
            s+=2**count
            print s
        count+=1
    return s

print binary_to_decimal("100001")
