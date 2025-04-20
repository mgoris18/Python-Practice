groceries = {
    "apple": 0.99,
    "banana": 0.59,
    "milk": 3.49,
    "bread": 2.89,
    "eggs": 2.99,
    "cheese": 4.50,
    "yogurt": 1.25
}
#Instructions:

#Ask the user how many different grocery items they are buying.
#For each item:
#Accept the item name.
#Accept the quantity (as an integer).
#Calculate the total grocery cost.
#Output the total as:
#Total grocery cost: $[amount]
#(rounded to 2 decimal places)

grocery_items = int(input())

grocery_items = int(input())

total_price = 0

for i in range(grocery_items):
    grocery_type = input()
    grocery_quantity = int(input())
    total_price += groceries[grocery_type] * grocery_quantity

print(f"Total grocery cost: ${total_price:.2f}")