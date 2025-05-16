#Accept two numbers to divide
numberOne = int(input())
numberTwo = int(input())

try:
    result = numberOne / numberTwo
    print(result)
except ZeroDivisionError:
    print('Error. Cannot divide by zero.')