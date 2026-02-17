data = [18, -4, 27, 9, 3]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is strictly between the minimum and maximum values when compared to data

num = int(input())
maxNum = max(data)
minNum = min(data)

ranked = minNum < num < maxNum

print(f"Between Min and Max? {ranked}")