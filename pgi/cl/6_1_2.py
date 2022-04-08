from unittest import async_case


def mult(m,n):
    if (n > 0):
        return m + mult(m,n-1)
    else:
        return 0

def mult2(m,n):
    def loop(n,ans):
        if (n > 0):
            return loop(n-1,m+ans)
        else:
            return ans
    return loop(n, 0)

def mult3(m,n):
    ans = 0
    while (n > 0):
        ans += m
        n -= 1
    return ans

print(mult3(4,5)) 