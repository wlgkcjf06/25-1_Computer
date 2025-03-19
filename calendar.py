def get_month():
    m= int(input('Enter a month(1~12). Enter 0 to exit program.'))
    while m<0 or m>12:
        m= int(input('Invalid input. Enter a number between 0 and 12.'))
    return m

def get_year():
    y=int(input('Enter a year between 1800 and 2099'))
    while y<1800 or y>2099:
        y=int(input('Invalid input. Enter a number between 1800 and 2099.'))
    return y

def ifleap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False


def zeller(month,year):
    if month <= 2:
        month = month + 12
        year = year - 1
    y = year % 100
    c = year // 100
    sday = (1 + ((month + 1) * 13)//5 + y + y//4 + c//4 - 2 * c) % 7
    return sday

while 1:
    month = get_month()
    if month ==0:
        break
    year = get_year()
    leap = ifleap(year)
    if month in [1,3,5,7,8,10,12]:
        days = 31
    elif month in [4,6,9,11]:
        days = 30
    elif month ==2 and leap:
        days = 29
    else:
        days = 28
    startday = zeller(month, year)
