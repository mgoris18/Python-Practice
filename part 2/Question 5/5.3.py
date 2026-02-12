def deposit(amount, balance):
    # TODO: Write assert so deposit amount must be > 0 using message:
    # "Deposit amount must be positive!"
    assert amount > 0, "Deposit amount must be positive!"

    return balance + amount

if __name__ == '__main__':
    amount = int(input())
    try:
        print(f"Your new balance is {deposit(amount, 100)}")
    except AssertionError as msg:
        print(msg)
