#solution accepts a 9-digit student ID as input (no dashes)
#solution outputs the ID in the format last4-first3-middle2

number = input()

last4 = number[5:9]
first3 = number[0:3]
middle2 = number[3:5]

print(f"{last4}-{first3}-{middle2}")