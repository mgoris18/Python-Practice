#solution accepts three integer values representing principal, rate, and time
#solution outputs the simple interest in dollars using formula I = (p * r * t) / 100

p = int(input())
r = int(input())
t = int(input())

interest_value = float((p * r * t) / 100)

print(f"Simple interest: {interest_value} dollars")

