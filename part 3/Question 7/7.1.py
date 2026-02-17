numbers = [12, -5, 8, 41, 3]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is less than the minimum value when compared to numbers

num = int(input())

result =  (num < min(numbers))

print(f"Less Than Min? {result}")