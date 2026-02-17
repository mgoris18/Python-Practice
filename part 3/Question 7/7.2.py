values = [7, 22, -9, 14, 0]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is equal to the maximum value when compared to values

num = int(input())
maxNum =( num == max(values))
print(f"Equal To Max? {maxNum}")