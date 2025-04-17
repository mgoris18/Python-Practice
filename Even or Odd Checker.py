#ask user to input a number
num1 = int(input("Input a number to check if it's even or odd: "))

#if loop to check if number is even or odd using modulo
def evenOrOdd(n):
    if n % 2 == 0:
        print('even')
    else: 
        print ('odd')
#call function
evenOrOdd(num1)
