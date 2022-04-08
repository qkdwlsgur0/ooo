def trinum(n):
    if n > 0:
        return trinum(n-1)+n
    else:
        return 0

def trinum2(n):
    def loop(n,total):
        if n > 0:
            return loop(n-1,total+n)
        else:
            return total
    return loop(n,0)

def trinum3(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(trinum3(4))