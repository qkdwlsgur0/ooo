from datetime import date
today = date.today()

def check_adult(year,month,day):
    return today.year-year > 19 or today.year-year == 19 and today.month-month > 0 \
           or today.year-year == 19 and today.month-month == 0 and today.day-day >= 0


print(check_adult(2003,4,21))