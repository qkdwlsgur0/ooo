def sigma_power_of_2_1(n):
    if n >= 0:
        return sigma_power_of_2_1(n-1)+2**n
    else:
        return 0

def sigma_power_of_2_2(n):
    def loop(n,total):
        if n >= 0:
            return loop(n-1,total+2**n)
        else:
            return total
    return loop(n,0)

def sigma_power_of_2_3(n):
    total = 0
    while n >= 0:
        total += 2**n
        n -= 1
    return total

def sigma_power_of_2(n):
    return 2**(n+1)-1

# sigma_power_of_2(n)
# n = 0
# sigma_power_of_2(0) == 2^(0+1)-1
#                     == 2^1-1
#                     == 1
#                     == 2^0
#
# 임의의 수 k에 대해 sigma_power_of_2(k) == 2^(k+1)-1이 참이라고 할 때,
#
# sigma_power_of_2(k+1) == 2^(k+1+1)-1 임을 증명
#
# sigma_power_of_2(k+1) == sigma_power_of_2(k) + 2^(k+1)
#                       == 2^(k+1)-1+2^(k+1)
#                       == 2*2^(k+1)-1
#                       == 2^(k+1+1)-1

print(sigma_power_of_2_1(0))
print(sigma_power_of_2_2(0))
print(sigma_power_of_2_3(0))