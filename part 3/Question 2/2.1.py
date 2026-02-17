
Totalounces = int(input())

ton = Totalounces // 32000

remaining = Totalounces % 32000

pounds = remaining // 16

ounces = remaining % 16


print(f"Tons: {ton}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")