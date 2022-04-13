from time import sleep
def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        sleep(1)
    print('Launch!')

countdown(1)

def sigma(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sigma(10))

def sumrange(m,n):
    sum = 0
    for i in range(m, n+1):
        sum += i
    return sum

print(sumrange(11,100))

def fac(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

print(fac(4))

def power(b,n):
    prod = 1
    for _ in range(n):
        prod *= b
    return prod

print(power(2,10))