if __name__ == '__main__':

    year = input()

    try:
        # validate year is integer
        # validate range
        year = int(year)
        if 1900 <= year <= 2025:
            print(f"Year recorded: {year}.")
        else:
            print("Year must be between 1900 and 2025")
        
    except ValueError:
        print("Year must be numeric.")
