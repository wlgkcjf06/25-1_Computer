def ifprime(n):
    k=2
    if n == 1: return False
    while k**2 <= n:
        if n%k==0:
            return False
        k+=1
    return True

def getprime(l,u):
    lst = []
    for i in range(l, u+1):
        pr = ifprime(i)
        if pr:
            lst.append(i)
    return lst

def totalcount(lst):
    tot=0
    for k in lst:
        tot=tot+k
    return tot

def maxminusmin(lst):
    lst.sort()
    a= (lst[len(lst)-1]-lst[0])
    return a

def odddigit(lst):
    oddnum = []
    for p in range(len(lst)):
        o = True
        for q in str(lst[p]):
            if int(q)%2==0:
                o = False
        if o:
            oddnum.append(lst[p])
    return oddnum

lb=int(input('Enter lower bound: '))
ub=int(input('Enter upper bound: '))

prime = getprime(lb,ub)

print('\nPrime numbers between',lb,'and',ub,':')
print(prime)

print('\nNumber of prime numbers:',len(prime))

print('\nTotal sum of prime numbers:',totalcount(prime))

print('\nMax - Min of prime numbers:',maxminusmin(prime))

print('\nPrime numbers that only contain odd digits:\n',odddigit(prime))



