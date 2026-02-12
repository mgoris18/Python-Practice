import hashlib

def hash_value(data):
    encoded = data.encode()
    h = hashlib.sha3_256()
    h.update(encoded)

    # TODO: fix this return value so output is hexadecimal, not binary
    return h.hexdigest()


if __name__ == "__main__":
    val = input()
    print(hash_value(val))
