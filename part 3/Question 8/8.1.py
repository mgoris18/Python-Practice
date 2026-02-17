languages = ["Python", "Java", "C++", "JavaScript", "Go"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

index = int(input())

try:
    print(languages[index])

except:
    print("Error")
