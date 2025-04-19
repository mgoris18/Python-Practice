#Covert cents into the largest possible number of dollats and remaining cents
#accept total number of cents as input

totalCents = int(input())

dollars = totalCents // 100

cents = totalCents % 100

print("Dollars:", dollars)
print("Cents:", cents)