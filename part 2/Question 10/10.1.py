# validate password length and digit requirement

if __name__ == '__main__':

    password = input()

    # strip whitespace
    password = password.strip()

    # check length requirement
    if len(password) < 8:
        print("Password must be at least 8 characters.")
    
    # check digit requirement
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
    
    else:
        print("Password accepted.")
