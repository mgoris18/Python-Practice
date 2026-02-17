#Product A: 12.50
#Product B: 9.99
#Product C: 4.75
#solution accepts three integer inputs representing quantities sold
#solution outputs "Revenue: " followed by total value to two decimal places


x = int(input())
y = int(input())
z = int(input())

a = 12.50
b = 9.99
c = 4.75

totalA = x * a

totalB = y * b

totalC = z * c

total = totalA + totalB + totalC

print(f"Revenue: {total:.2f} dollars")