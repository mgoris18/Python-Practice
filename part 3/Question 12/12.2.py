filename = input()

with open(filename, "r") as file:
    numbers = file.read().splitlines()

sum = sum(numbers)

with open(filename, "a") as file:
    file.write("\n" + sum)

with open(filename, "r") as file:
    print(file.read())