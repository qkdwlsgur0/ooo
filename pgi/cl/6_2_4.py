#제곱

def square(n):
    def loop(n):
        if n > 0:
            return square(n-1)+(n+n-1)
        else:
            return 0
    return loop(abs(n))

def square2(n):
    def loop(n,total):
        if n > 0:
            return loop(n-1,total+(n+n-1))
        else:
            return total
    return loop(abs(n),0)

def square3(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += (n+n-1)
        n -= 1
    return total

print(square(3))



# square(n)의 답이 항상 n^2이 되는지 증명하시오
# (기초)
# n = 0
# square(0) == 0^2

# (귀납)
# 가정 k < n인 임의의 k에 대해서,
#     square(k) == k^2

# square(k+1) == (k+1)^2 임을 증명하면 됨
# square(k+1) == square(k) + k+1 + k+1 - 1
#             == k^2 + 2 * k + 1
#             == (k + 1)^2
#             == square(k+1)