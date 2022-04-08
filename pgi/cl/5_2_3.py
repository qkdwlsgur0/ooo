def power(m,n):
    if n > 0:
        return m*power(m,n-1)
    else:
        return 1

def power2(m,n):
    def loop(m,n,prod):
        if n > 0:
            return loop(m,n-1,m*prod)
        else:
            return prod
    return loop(m,n,1)

def power3(m,n):
    prod = 1
    while n > 0:
        n -= 1
        prod *= m
    return prod

def power4(m,n):
    if n > 0:
        if n%2 == 0:
            return power4(m*m,n/2)
        else:
            return m*power(m,n-1)
    else:
        return 1

def power5(m,n):
    def loop(m,n,prod):
        if n > 0:
            if n%2 == 0:
                return loop(m*m,n/2,prod)
            else:
                return loop(m,n-1,prod*m)
        else:
            return prod
    return loop(m,n,1)

def power6(m,n):
    prod = 1
    while n > 0:
        if n%2 == 0:
            m *= m
            n /= 2
        else:
            n -= 1
            prod *= m
    return prod

print(power6 (2,11))
