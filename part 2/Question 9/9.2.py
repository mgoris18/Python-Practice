if __name__ == '__main__':

    salary = input()

    try:
        # TODO: validate salary is integer
        salary = int(salary)

        print(f"Your salary is {salary}.")

    except:
        print("Salary must be a number.")
