def validclock12(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]
    return (len(hour) == 1 and 1 <= int(hour) <= 9 or \
            len(hour) == 2 and 10 <= int(hour) <= 12) and \
           colon == ":" and \
           len(minute) == 2 and 0 <= int(minute) <= 59 and \
           (am_or_pm == "am" or am_or_pm == "pm")

print(validclock12("1:30am"))  # True
print(validclock12("9:12pm"))  # True
print(validclock12("3:05am"))  # True
print(validclock12("10:14pm")) # True
print(validclock12("11:59pm")) # True
print(validclock12("12:00am")) # True
print(validclock12("12:00pm")) # True
print(validclock12("0:15am"))  # False
print(validclock12("09:18pm")) # False
print(validclock12("3:5am"))   # False 
print(validclock12("00:00pm")) # False
print(validclock12("5:60am"))  # False

