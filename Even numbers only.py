N = int(input("Input a number: "))

allNums = []

#define function to list all numbers from 1 to N
def arrayNum(x):
    for i in range(1,x+1):
        allNums.append(i)
    
arrayNum(N)

#define function to list the even numbers
def evenNum(y):
    for i in allNums:
        if i % 2 == 0:
            print(i)

evenNum(N)


