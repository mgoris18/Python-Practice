#covert total days into weeks and days
#accept total days as input

total_days = int(input())

weeks = total_days // 7

days = total_days % 7

print("Weeks:",weeks)
print("Days:",days)