
def multiply_numbers(a,b):
    if a is None:
        print("a is a null value")
        return b
    if b is None:
        print("b is a null value")
        return a
    return(a * b)


multiply_numbers(5, None)
