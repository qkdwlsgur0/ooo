def sigma(n):
    if n > 0:
        return sigma(n-1)+n
    else:
        return 0


def sigma2(n):
    def loop(n, total):
        if n > 0:
            return loop(n-1,n+total)
        else:
            return total
    return loop(n,0)


def sigma3(n):
    total = 0
    while n > 0:
        n, total = n-1, n+total
    return total