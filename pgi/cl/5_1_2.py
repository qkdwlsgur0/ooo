def validclock24(time):
    (hour, colon, minute) = time.partition(":")
    return len(hour) == 2  and len(minute) == 2 and colon == ":" and\
           0 <= int(hour) <= 23 and 0 <= int(minute) <= 59 or\
           int(hour) == 24 and int(minute) == 0

print(validclock24("00:00"))
print(validclock24("00:30"))
print(validclock24("09:58"))
print(validclock24("12:15"))
print(validclock24("23:59"))
print(validclock24("24:00"))
print(validclock24("7:07"))
print(validclock24("07:121"))
print(validclock24("13:4"))
print(validclock24("00:60"))
print(validclock24("24:01"))
print(validclock24("25:10"))