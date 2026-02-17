movies = {
    "action": 12.50,
    "comedy": 10.00,
    "drama": 11.25,
    "horror": 9.75,
    "sci-fi": 13.40
}

#discount tiers: <5 no discount, 5-10 (inclusive) 7%, >10 15%
#solution accepts string movie title
#solution accepts integer ticket quantity
#solution outputs movie title and total cost to 2 decimal places


movie = input()
quantity = int(input())
discount = 0

if quantity < 5:
    total = quantity * movies[movie]
    print(f"{movie} ${total:.2f}")
elif 5 <= quantity <= 10:
    for i in range(quantity):
        discount += movies[movie] * 0.07
    total = (quantity * movies[movie]) - discount
    print(f"{movie} ${total:.2f}")
elif quantity > 10:
    for i in range(quantity):
        discount += movies[movie] * 0.15
    total = (quantity * movies[movie]) - discount
    print(f"{movie} %{total:.2f}")