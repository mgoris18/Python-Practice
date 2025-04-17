#ask user for number N
N = int(input("Input a number: "))

#define a function that creates a loop to print all numbers from 1 to n

def oneToN(num):
    for i in range(1, num+1):
        print(i)
oneToN(N)