def greet_user(username):
    # TODO: Write assert to ensure username is not empty using message:
    # "Username cannot be empty!"
    assert len(username) != 0, "Username cannot be empty!"
    

    return f"Welcome, {username}!"

if __name__ == '__main__':
    username = input()
    try:
        print(greet_user(username))
    except AssertionError as msg:
        print(msg)
