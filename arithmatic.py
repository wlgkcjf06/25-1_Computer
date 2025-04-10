## Four basic arithmetic calculator ##
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def multiply(a,b):
    return a * b

def divint(i):
    if i == 0:
        return False
    else:
        return True

def divide(a,b):
    if divint(b):
        return a / b
    else:
        return 'Error: Cannot divide by zero'

def calculate(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a,b)
    elif op == '*':
        return multiply(a,b)
    elif op == '/':
        return divide(a,b)

def main():
    print("Welcome to the Four Basic Calculator! (Type 'q' to quit)")
while True:
    user_input = input("Enter calculation (e.g., 5 + 3): ")
    if user_input.lower() == 'q':
        print("Adios!")
        break
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please enter in the form: a + b")
        continue
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    result = calculate(num1, num2, op)
    print("Result:", result)

main()