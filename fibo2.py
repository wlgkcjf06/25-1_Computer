warea = [0 for i in range(100)]
def fibo(i):
    if i<=1:
        return i
    elif warea[i+1]!=0:
        return warea[i+1]
    else:
        warea[i+1]=fibo(i-1)+fibo(i-2)
        return warea[i+1]


print('This program will display n-th number in Fibonacci sequence.')
n=int(input('Enter a number n: '))
number = fibo(n)
if n%10==1 and n!=11:
    print(n, 'st number in Fibonacci sequence is', number)
elif n%10==2 and n!=12:
    print(n, 'nd number in Fibonacci sequence is', number)
elif n%10==3 and n!=13:
    print(n, 'rd number in Fibonacci sequence is', number)
else:
    print(n, 'th number in Fibonacci sequence is', number)