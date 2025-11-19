'''
Topic: Assign variables, arithmetic, formatted output
Task:
You are given three integer inputs representing how many deliveries each driver makes in one day.
Each driver travels a fixed number of miles per delivery:
Driver X: 12.75 miles
Driver Y: 8.40 miles
Driver Z: 19.30 miles
Calculate the total miles traveled and output it to two decimal places.
'''

driverX = 12.75
driverY = 8.40
driverZ = 19.30

driverXD = int(input())
driverYD = int(input())
driverZD = int(input())

total = (driverX * driverXD) + (driverY * driverYD) + (driverZ * driverZD)

print(f"Total miles: {total:.2f}")