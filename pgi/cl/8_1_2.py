#펠린드롬 검사 함수

def ispalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return ispalindrome(s[1:-1])
    else:
        return False

def ispalindrome(s):
    return len(s) <= 1 or s[0] == s[-1] and ispalindrome(s[1:-1])


#삼각수 for로

def trinum(n):
    total = n
    for i in range(n):
        total += i
    return total


#덧셈만으로 제곱 계산 for로

def square(n):
    n = abs(n)
    sum = 0
    for i in range(1,n+1):
        sum += i+i-1
    return sum


#updown재귀함수를 꼬리재귀 while루프 for루프로 (짝수 0.5배 홀수 2배)

def updown(ns):
    if ns != []:
        if ns[0]%2 == 0:
            return [ns[0]//2]+updown(ns[1:])
        else:
            return [ns[0]*2]+updown(ns[1:])
    else:
        return []

def updown(ns):
    def loop(ns,ss):
        if ns != []:
            if ns[0]%2 == 0:
                ss.append(ns[0]//2)
            else:
                ss.append(ns[0]*2)
            return loop(ns[1:],ss)
        else:
            return ss
    return loop(ns,[])

def updown(ns):
    ss = []
    while ns != []:
        if ns[0]%2 == 0:
            ss.append(ns[0]//2)
        else:
            ss.append(ns[0]*2)
        ns = ns[1:]    
    return ss

def updown(ns):
    ss = []
    for n in ns:
        if n%2 == 0:
            ss.append(n//2)
        else:
            ss.append(n*2)
    return ss
