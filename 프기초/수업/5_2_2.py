def sumrange(m, n):
    if n >= m:
        return m+sumrange(m+1,n)
    else:
        return 0

def sumrange2(m, n):
    def loop(m, n, total):
        if n >= m:
            return loop(m+1, n, m+total)
        else:
            return total
    return loop(m, n, 0)


def sumrange3(m, n):
    total = 0
    while n >= m:
        total += m
        m += 1
    return total

print(sumrange3(11,100))