def get_month():
    m= int(input('Enter a month(1~12). Enter 0 to exit program.\nInput: '))
    while m<0 or m>12:
        m= int(input('Invalid input. Enter a number between 0 and 12.\nInput: '))
    return m

def get_year():
    y=int(input('Enter a year between 1800 and 2099.\nInput: '))
    while y<1800 or y>2099:
        y=int(input('Invalid input. Enter a number between 1800 and 2099.\nInput: '))
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

def shiftdays(d):
    if d==0:
        d=6
    else:
        d=d-1
    return d

def displaycalendar(arr):
    print('Sun Mon Tue Wed Thu Fri Sat')
    c=1
    for i in range(6):
        for j in range(7):
            if arr[i][j]==0:
                print('    ',end='')
            else:
                if c<=9:
                    print('  '+str(arr[i][j])+' ',end="")
                    c=c+1
                else:
                    print(' '+str(arr[i][j])+' ',end='')
        print('')



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
    startday = shiftdays(startday)
    arr=[]
    counter = 1
    for i in range(6):
        arr.append([])
        for j in range(7):
            arr[i].append(0)
            if i == 0:
                if j>=startday:
                    arr[i][j]=counter
                    counter=counter+1
            else:
                if counter<=days:
                    arr[i][j]=counter
                    counter=counter+1
    displaycalendar(arr)


