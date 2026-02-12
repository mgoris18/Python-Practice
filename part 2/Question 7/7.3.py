import hashlib

def secure_hash(pwd):
    # TODO: encode the password
    encoded = pwd.encode()
    h = hashlib.sha3_256()
    h.update(encoded)
    return h.hexdigest()
    # TODO: create hash object
    

    # TODO: update hash with encoded password
    

    # TODO: return hex digest
    

if __name__ == "__main__":
    p = input()
    print(secure_hash(p))
