def fac(n):
    if n > 0:
        return n*fac(n-1)
    else:
        return 1

def fac2(n):
    def loop(n,m):
        if n > 1:
            return loop(n-1,m*n)
        else:
            return m
    return loop(n,1)

def fac3(n):
    m = 1
    while n > 1:
        m *= n
        n -= 1
    return m

print(fac(5))
print(fac2(6))
print(fac3(7))