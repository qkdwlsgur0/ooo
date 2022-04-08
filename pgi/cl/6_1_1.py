def gcd(m,n):
    if (n != 0):
        return gcd(n,m%n)
    else:
        return m 

def gcd2(m,n):
    while (n != 0):
        m, n = n, m%n
    return m
    
def gcd3(m,n):
    def loop(m,n,k):
        if not (m == 0 or n == 0):
            if m % 2 == 0 and n % 2 == 0:
                return loop(m//2,n//2,2*k)
            elif m % 2 == 0 and n % 2 == 1:
                return loop(m//2,n,k)
            elif m % 2 == 1 and n % 2 == 0:
                return loop(m,n//2,k)
            elif m <= n:
                return loop(m,(n-m)//2,k)
            else:
                return loop(n,(m-n)//2,k)
        else:
            if m == 0:
                return n*k
            else:
                return m*k
    return loop(m,n,1)

def gcd4(m,n):
    k = 1
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            m, n, k = m // 2, n // 2, 2 * k
        elif m % 2 == 0 and n % 2 == 1:
            m = m // 2
        elif m % 2 == 1 and n % 2 == 0:
            n = n // 2
        elif m <= n:
            n = (n - m) // 2
        else:
            m, n = n, (m - n) // 2
    if m == 0:
        return n*k
    else:
        return m*k



print(gcd2(18,45)) 