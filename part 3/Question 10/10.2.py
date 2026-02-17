books = {
    'Math': 45.50,
    'Science': 38.75,
    'History': 29.99,
    'Art': 22.40,
    'Music': 18.60
}

#solution accepts an integer input representing the number of book selections
#solution accepts string inputs equivalent to the integer input identifying the book selections
#solution outputs the total price as "Total price: $" followed by the total cost to 2 decimal places

num = int(input())

total = 0

for i in range(num):
    selection = input()
    total += books[selection]

print(f"Total price: ${total}:.2f")