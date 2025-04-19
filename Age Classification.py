#Write a program that accepts an integer representing someone's age and classifies them as follows:
#0 to 2 years old: Infant
#3 to 12 years old: Child
#13 to 17 years old: Teenager
#18 to 64 years old: Adult
#65 or older: Senior

#Additionally, handle edge cases:
#If the input is less than 0, return: "Age cannot be negative"
#If the input is greater than 150, return: "Age seems too high"
age = int(input())

if age < 0:
    print("Age cannot be negative")
elif age > 150:
    print("Age seems too high")
elif 0 <= age <= 2:
    print("Infant")
elif 3 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age <= 64:
    print("Adult")
else:
    print("Senior")
