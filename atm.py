def setpassword():
    p=input('Set a 4-digit numeric password: ')
    while len(p)!=4 and (not p.isdigit()==4):
        p=input('Password must be exactly 4 digits. Try again: ')
    print('Password has been set.')
    return int(p)

def menu():
    print('--- ATM MENU ---\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit')
    i=int(input('Select an option: '))
    return i

def checkpw(p):
    a = 3
    t = False
    while 1:
        i= int(input('Enter your password to proceed with withdrawal: '))
        if i!=p:
            a-=1
            print('Incorrect Password. '+str(a)+' attempt(s) remaining.')
        if i == p:
            t = True
            break
        if a == 0:
            print('Password entered incorrectly 3 times. Withdrawal cancelled')
            break
    return t




print('Welcome to the ATM.')
pw = setpassword()
bal = 100000
while 1:
    me = menu()
    if me == 1:
        print('Your current balance is '+str(bal)+' won.')
    elif me == 2:
        correctpw = checkpw(pw)
        if correctpw:
            wa=int(input('Enter the amount to withdraw: '))
            if wa % 1000 != 0:
                print('Withdrawal must be in units of 1000 won.')
            else:
                if wa > bal:
                    print('Insufficient balance.')
                else:
                    bal = bal - wa
                    print('Withdrawal successful. Current balance: '+str(bal)+' won')
    elif me == 3:
        da = int(input('Enter the amount to deposit: '))
        if da%1000==0:
            bal = bal + da
            print('Deposit successful. Current balance: '+str(bal)+' won')
        else:
            print('Deposit must be in units of 1000 won.')
    elif me == 4:
        break
