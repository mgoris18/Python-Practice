#there are 12 inches in a foot and 3 feet in a yard
#solution accepts an integer value representing any number of inches
#solution outputs the converted yards, feet, and inches represented by the input value of inches

inches = int(input())

Yards = inches // 36

remaining = inches % 36

feet = remaining // 12

remaining = remaining % 12

print(f"Yards: {Yards}")
print(f"Feet: {feet}")
print(f"Inches: {remaining}")