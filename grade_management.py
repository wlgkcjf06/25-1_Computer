def printmenu():
    print("\n==========================")
    print("1. Add a new student")
    print("2. Search for a student")
    print("3. Rank of all students")
    print("4. Exit")
    print("==========================")

def enterstd():
    na=input("Enter the student's name: ")
    kr = int(input("Enter the student's korean score: "))
    en = int(input("Enter the student's english score: "))
    ma = int(input("Enter the student's math score: "))
    return[na,kr,en,ma]

def getrank(dic):
    totd = {}
    for key in dic:
        ws = dic[key]
        stot = 0
        for i in range(len(ws)):
            stot=stot+ws[i]
        totd[key]=stot
    srtd = sorted(totd.items(), key = lambda x:x[1], reverse = True)
    print(srtd)
    print('name | rank')
    for i in range(len(srtd)):
        print(f"{srtd[i][0]:4} | {i+1}")

grades = {"John":[100,96,94],"Jane":[92,100,90]}

while 1:
    printmenu()
    menui = input('Enter your option(1-4): ')
    if menui == '1':
        sdata = enterstd()
        grades[sdata[0]]=sdata[1:4]
    elif menui == '2':
        name=input("Enter the student's name to search: ")
        tmp = grades[name]
        tot = 0
        for i in range(3):
            tot=tot+tmp[i]
        avg = format(tot/3,'.1f')
        print("name | kor | eng | math | total | avg")
        print(f"{name:>4} |{tmp[0]:>4} |{tmp[1]:>4} |{tmp[2]:>5} |{tot:>6} |{avg:>4}")
    elif menui == '3':
        rank = getrank(grades)
    elif menui == '4':
        print('Exiting the program.')
        break