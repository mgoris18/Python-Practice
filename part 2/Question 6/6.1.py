def check_alpha_value(value):
    # TODO: return True if alphabetic, else False
    return str(value).isalpha()

def check_null_string(text):
    # TODO: return True if text is not None, else False
    return text is not None


if __name__ == "__main__":
    text = input()
    alpha = input()

    print(check_null_string(text))
    print(check_alpha_value(alpha))
