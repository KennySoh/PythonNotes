def diff(p):
    dp={}
    for j in p.keys():
        if j!=0:
            dp[j-1]=j*p[j]
    return dp


