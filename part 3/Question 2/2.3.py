inches = 50

yards = inches // 36
remaining = inches % 36

feet = remaining // 12
inches_left = remaining % 12

print(f"Yards: {yards}")
print(f"Feet: {feet}")
print(f"Inches: {inches_left}")
