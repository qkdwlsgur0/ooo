from datetime import date

def check_adult(year, month, day):
    from datetime import date
    today = date.today()
    return int(today.year)-int(year) >= 20 or\
           int(today.year)-int(year) == 19 and\
           (int(today.month)-int(month) > 0 or\
           int(today.month)-int(month) == 0 and\
           (int(today.day)-int(day) > 0 or\
           int(today.day)-int(day) == 0))
   
today = date.today()
year = today.year
month = today.month
day = today.day
print(today)
print(check_adult(year-20,12,31))
print(check_adult(year-19,month-1,1))
print(check_adult(year-19,month,day-1))
print(check_adult(year-19,month,day))
print(check_adult(year-19,month,day+1))
print(check_adult(year-19,month+1,1))