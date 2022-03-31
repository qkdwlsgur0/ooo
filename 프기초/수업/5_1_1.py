def isleapyear(n):
    if (n >= 0):
        return n%4 == 0 and n%100 != 0 or n%400 == 0
    else:
        return None
        
print(isleapyear(2022))