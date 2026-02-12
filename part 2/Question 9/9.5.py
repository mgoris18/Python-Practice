if __name__ == '__main__':

    product_id = input()

    try:
        product_id = product_id.strip()

        # validate numeric
        int(product_id)

        # validate length
        if len(product_id) == 6:
            print(f"Product ID accepted: {product_id}.")
        else:
            print("Product ID must be exactly 6 digits.")

    except ValueError:
        print("Product ID must be numeric.")
