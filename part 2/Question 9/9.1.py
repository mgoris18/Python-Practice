if __name__ == '__main__':

    age = input()

    try:
        # TODO: validate age is integer
        age = int(age)

        print(f"Your age is {age}.")

    except:
        
        print("Age must be numeric.")
