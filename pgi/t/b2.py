from datetime import date
today = date.today()

def how_ord(year,month,day):
    if  today.month-month > 0 or \
        today.month-month == 0 and today.day-day >= 0:
        return today.year-year
    else:
        return today.year-year-1
    
