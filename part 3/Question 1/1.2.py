#Package A: 5.25
#Package B: 8.60
#Package C: 3.75
#solution accepts three integer inputs
#solution outputs "Shipping: " followed by total value to two decimal places

a = int(input())
b = int(input())
c = int(input())

PA = 5.25
PB = 8.60
PC = 3.75

total =(a * PA) + (b * PB) + (c * PC)

print(f"Shipping: {total:.2f}, dollars")
