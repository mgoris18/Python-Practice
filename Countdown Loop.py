#define whaat number we'll be counting down from
num = 5

#define countdown funtion
def countdown(n):
    #range() generates a sequence of numbers. range(start,stop,step) 
    #So basically in my code it starts at n- which is 5 in this case,
    #stops at 0 which is not printed, and decreases by 1 in each iteration.
    for i in range(n,0,-1):
        print(i)

#call function
countdown(num)
