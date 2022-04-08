def fastmult(m,n):
    if n > 0:
        if n%2 == 0:
            return fastmult(m+m,n//2)
        else:
            return m+fastmult(m,n-1)
    else:
        return 0

def fastmult2(m,n):
    def loop(m,n,ans):
        if n > 0:
            if n%2 == 0:
                return loop(m+m,n/2,ans)
            else:
                return loop(m,n-1,ans+m)
        else:
            return ans
    return loop(m,n,0)

def fastmult3(m,n):
    ans = 0
    while n > 0:
        if n%2 == 0:
            m, n = m+m, n/2
        else:
            n, ans = n-1, ans+m
    return ans 

print(fastmult3(4,5))