#Write a program that takes an integer representing a student's grade and classifies it as follows:
#90 or above: A
#80 to 89: B
#70 to 79: C
#60 to 69: D
#Below 60: F

#Additionally, handle edge cases:
#If the grade is below 0, return: "Grade cannot be negative"
#If the grade is above 100, return: "Grade cannot exceed 100"

grade = int(input())

if grade < 0:
    print("Grade cannot be negative")
elif grade > 100:
    print("Grade cannot exceed 100")
elif  grade >= 90:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
else:
    print("F")