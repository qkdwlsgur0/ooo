def russian_mult(m,n):
    if n > 0:
        if n%2 == 1:
            return m+russian_mult(m*2,n//2)
        else:
            return russian_mult(m*2,n//2)
    else:
        return 0

def russian_mult2(m,n):
    def loop(m,n):
        if n > 1:
            if n%2 == 1:
                return print(m+russian_mult(m*2,n//2))
            else:
                return print(russian_mult(m*2,n//2))
        else:
            return m
    if n > 0:
        return loop(m,n)
    else:
        return 0

def russian_mult3(m,n):
    def loop(m,n,total):
        if n > 0:
            if n%2 == 1:
                return loop(m*2,n//2,total+m)
            else:
                return loop(m*2,n//2,total)
        else:
            return total
    return loop(m,n,0)

def russian_mult4(m,n):
    ans = 0
    while n > 0:
        if n%2 == 1:
            ans += m
            m *= 2
            n //= 2
        else:
            m *= 2
            n //= 2
    return ans


print(russian_mult4(57,0))