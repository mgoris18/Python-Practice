def check_uppercase(text):
    # TODO: return True if text is all uppercase letters, else False
    return str(text).isupper()

def check_null_string(text):
    # TODO: return True if text is not None, else False
    return text is not None

if __name__ == "__main__":
    text1 = input()
    text2 = input()

    print(check_null_string(text1))
    print(check_uppercase(text2))
