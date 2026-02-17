menu = {
    'Burger': 8.99,
    'Fries': 3.49,
    'Shake': 4.25,
    'Salad': 6.75,
    'Soda': 1.99
}

#solution accepts an integer input representing the number of menu selections
#solution accepts string inputs equivalent to the integer input identifying the menu selections
#solution outputs the total cost as "Total cost: $" followed by the total cost to 2 decimal places
num = int(input())
total = 0

for i in range(num):
    selection = input()
    total += menu[selection]

print(f"Total cost: ${total:.2f}")