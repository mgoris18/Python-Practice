#solution accepts hours (int), wage (float), tax rate (int)
#solution outputs "Net Pay: " followed by net amount to two decimal places


a = int(input())
b = float(input())
c = int(input())

gross = a * b
tax = gross * (c / 100)
net = gross - tax

print(f"Net Pay: {net:.2f} dollars")