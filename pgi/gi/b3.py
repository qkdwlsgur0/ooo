def sigma_even(n):
    if n > 0:
        return 2*n+sigma_even(n-1)
    else:
        return 0

def sigma_even(n):
    def loop(n,total):
        if n > 0:
            return loop(n-1,total+2*n)
        else:
            return total
    return loop(n,0)

def sigma_even(n):
    total = 0
    while n > 0:
        total += 2*n
        n -= 1
    return total

