# Fibonacci Program
# This program will display n-th number in Fibonacci sequence.
# program greeting
import math
print('This program will display n-th number in Fibonacci sequence.')
# get number
n = int(input('Enter a number n: '))
# calculate n-th Fibonacci number. (Hint: use if & while)
fibo = (((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/math.sqrt(5)
number = int(fibo)
if n%10==1 and n!=11:
    print(n, 'st number in Fibonacci sequence is', number)
elif n%10==2 and n!=12:
    print(n, 'nd number in Fibonacci sequence is', number)
elif n%10==3 and n!=13:
    print(n, 'rd number in Fibonacci sequence is', number)
else:
    print(n, 'th number in Fibonacci sequence is', number)