cities = ["Miami", "New York", "Dallas", "Seattle", "Boston"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

index = int(input())

try:
    print(cities[index])
except:
    print("Error")