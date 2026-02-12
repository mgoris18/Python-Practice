#check if the input range is between 20 and 30 for the range validation check

if __name__ == '__main__': 
        
    r = range(20,31)
    
    num = int(input())
    
    # create conditional statement for range check here
    if num in r:
        print("The number input is in the range from 20 and 30.")
    else: 
        print("The number input is not in the range from 20 and 30.")