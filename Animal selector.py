animals = ["Cat", "Dog", "Rabbit", "Parrot", "Lizard", "Turtle"]

#Output the animal name for the index given.
#Use a try block, and output "Invalid index" if the input is out of range or not valid.
#Print only the animal name or the error message.

index = int(input())

try:
    animals_index = animals[index]
    print(animals_index)
except:
    print("Invalid index")
