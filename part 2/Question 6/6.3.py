def check_spaces(text):
    # TODO: return True if text contains ONLY spaces, else False
    return text.strip() == ""


def check_null_string(text):
    # TODO: return True if text is not None, else False
    return text is not None

if __name__ == "__main__":
    text1 = input()
    text2 = input()

    print(check_null_string(text1))
    print(check_spaces(text2))
