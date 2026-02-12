def process_age(age):
    # TODO: Write assert to block negative ages using message:
    # "Age cannot be negative!"
    assert age >= 0, "Age cannot be negative!"


    return age * 2

if __name__ == '__main__':
    age = int(input())
    try:
        print(process_age(age))
    except AssertionError as msg:
        print(msg)
