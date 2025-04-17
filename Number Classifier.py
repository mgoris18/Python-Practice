num = int(input("Input a number: "))

#define a functio that will check if a number is positive or negative
def positiveOrNegative(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

positiveOrNegative(num)