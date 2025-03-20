#달 입력받기
def getmonth():
    m= int(input('Enter month (1-12): '))
    while (m<0 or m>12) and m != -1:
        m= int(input('INVALID INPUT - Enter month (1-12): '))
    return m

#년도 임력받기
def getyear():
    y=int(input('Enter year (yyyy): '))
    while y<1800 or y>2099:
        y=int(input('INVALID INPUT - Enter year (1800-2099): '))
    return y

#윤년인지 판단
def ifleap(y):
    if y%400==0:
        return True
    elif y%100==0:
        return False
    elif y%4==0:
        return True
    else:
        return False

def getdays(m, l):
    if m in [1,3,5,7,8,10,12]:
        d = 31
    elif month in [4,6,9,11]:
        d = 30
    elif month ==2 and l:
        d = 29
    else:
        d = 28
    return d

#입력받은 달이 시작하는 요일 구하기
def zeller(m,ye):
    if m <= 2:
        m += 12
        ye -= 1
    y = ye % 100
    c = ye // 100
    res = (1 + ((m + 1) * 13)//5 + y + y//4 + c//4 - 2 * c) % 7
    return res

#토요일 0 -> 일요일 0으로 바꾸기
def shiftdays(d):
    if d==0:
        d=6
    else:
        d=d-1
    return d

def getrows(s, d):
    k = (s+d)//7
    if s+d%7!=0:
        k+=1
    return k

def makearray(s, d, r):
    tmp=[]
    c = 1
    for i in range(r):
        tmp.append([])
        for j in range(7):
            tmp[i].append(0)
            if i == 0:
                if j>=s:
                    tmp[i][j]=c
                    c+=1
            else:
                if c<=d:
                    tmp[i][j]=c
                    c+=1
    return tmp

def displaymonthyear(m,y):
    mlist=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    mo=mlist[m-1]+' '+str(y)
    out=mo.center(20)
    print(out)

#달력 표시
def displaycalendar(mon,r):
    print('Su Mo Tu We Th Fr Sa')
    c=1
    for i in range(r):
        for j in range(7):
            if mon[i][j]==0:
                print('   ',end='')
            else:
                if c<=9:
                    print(' '+str(mon[i][j])+' ',end="")
                    c=c+1
                else:
                    print(str(mon[i][j])+' ',end='')
        print('')


print('This Program will display a calendar month between 1800 and 2099')
while 1:
    month = getmonth()
    if month == -1:
        break
    year = getyear()
    leap = ifleap(year)
    days = getdays(month, leap)
    startday = zeller(month, year)
    startday = shiftdays(startday)
    rows = getrows(startday, days)
    arr = makearray(startday, days, rows)
    displaymonthyear(month,year)
    displaycalendar(arr,rows)


