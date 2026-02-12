if __name__ == '__main__':

    quantity = input()

    try:
        # validate quantity is integer
        # validate quantity is > 0
        quantity = int(quantity)
        if quantity <= 0:
            print("Quantity must be greater than 0.")
        else:
            print(f"Quantity accepted: {quantity}")

    except ValueError:
        print("Quantity must be numeric.")
