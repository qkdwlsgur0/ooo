from operator import truediv


def isleapyear1(y):
    if (y >= 0):
        return y%4 == 0 and y%100 != 0 or y%400 == 0
    else:
        return None
        
def isleapyear2(y):
    if (y >= 0):
        if (y%4 == 0):
            if (y%100 == 0):
                if (y%400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return None

print(isleapyear2(2022))
print(isleapyear2(2000))
print(isleapyear2(2100))
print(isleapyear2(2024))
print(isleapyear2(-2839))