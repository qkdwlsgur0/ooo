def sigma_power_of_2(n):
    if n >= 0 :
        return 2**n+sigma_power_of_2(n-1)
    else:
        return 0


def sigma_power_of_2(n):
    def loop(n,ans):
        if n >= 0 :
            return loop(n-1, ans+2**n)
        else:
            return ans
    return loop(n,0)


def sigma_power_of_2(n):
    ans = 0
    while n >= 0:
        ans += 2**n
        n -= 1
    return ans

