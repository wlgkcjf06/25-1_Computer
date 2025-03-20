# GCD Program
# This program will display GCD of two integers.
# program greeting
print('This program will display GCD of two integers.')
# get numbers
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
# calculate GCD
if num2>num1:
    tmp = num1
    num1 = num2
    num2 = tmp

while 1:
    k=num1%num2
    if k==0:
        GCD=num2
        break
    num1=num2
    num2=k

print('GCD is', GCD)