'''
Topic: Variables, multiplication, addition, formatting
Task:
A warehouse records how many trips each cart makes.
You will receive three integer inputs:
Cart 1: 3.20 miles per trip
Cart 2: 5.50 miles per trip
Cart 3: 7.75 miles per trip
Compute the total miles traveled and output to two decimal places.
Output format:
Miles traveled: value miles
'''

cart1 = 3.20
cart2 = 5.50
cart3 = 7.75

cart1x = int(input())
cart2x = int(input())
cart3x = int(input())

total = (cart1 * cart1x) + (cart2 * cart2x) + (cart3 * cart3x)

print(f"Miles traveled: {total:.2f}")