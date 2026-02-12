#check if the input range is between 5 and 15 for the range validation check

if __name__ == '__main__': 
        
    r = range(5,15)
    
    num = int(input())
    
    # create conditional statement for range check here
    if num in r:
        print("The number input is in the range from 5 and 15.")
    else:
        print("The number input is not in the range from 5 and 15.")
