#달 입력받기
def get_month():
    m= int(input('Enter month (1-12): '))
    while (m<0 or m>12) and m != -1:
        m= int(input('INVALID INPUT - Enter month (1-12): '))
    return m

#년도 임력받기
def get_year():
    y=int(input('Enter year (yyyy): '))
    while y<1800 or y>2099:
        y=int(input('INVALID INPUT - Enter year (1800-2099): '))
    return y

#윤년인지 판단
def ifleap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False


#입력받은 달이 시작하는 요일 구하기
def zeller(month,year):
    if month <= 2:
        month = month + 12
        year = year - 1
    y = year % 100
    c = year // 100
    sday = (1 + ((month + 1) * 13)//5 + y + y//4 + c//4 - 2 * c) % 7
    return sday

#토요일 0 -> 일요일 0으로 바꾸기
def shiftdays(d):
    if d==0:
        d=6
    else:
        d=d-1
    return d

'''def removeemptyrow(arr):
    for i in range(6):
        check = False
        for j in range(7):
            if arr[i][j]!=0:
                check = True
        if check:'''


def displaymonthyear(m,y):
    mlist=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    mo=mlist[m-1]+' '+str(y)
    out=mo.center(20)
    print(out)

#달력 표시
def displaycalendar(arr,r):
    print('Su Mo Tu We Th Fr Sa')
    c=1
    for i in range(r):
        for j in range(7):
            if arr[i][j]==0:
                print('   ',end='')
            else:
                if c<=9:
                    print(' '+str(arr[i][j])+' ',end="")
                    c=c+1
                else:
                    print(str(arr[i][j])+' ',end='')
        print('')


while 1:
    print('This Program will display a calendar month between 1800 and 2099')
    month = get_month()
    if month == -1:
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
    if startday+days==28:
        rows = 4
    elif startday+days<=35:
        rows = 5
    else:
        rows = 6
    arr=[]
    counter = 1
    for i in range(rows):
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
    displaymonthyear(month,year)
    displaycalendar(arr,rows)


