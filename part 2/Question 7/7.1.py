import hashlib

def hash_password(pwd):
    # TODO: encode the password
    enc_pwd = pwd.encode()

    # TODO: create a secure hash object (NOT sha1, NOT sha256)
    d = hashlib.sha3_256()
    d.update(enc_pwd)
    return d.hexdigest()

    # TODO: update hash with encoded password
    

    # TODO: return the hex digest
    


if __name__ == "__main__":
    pwd = input()
    print(hash_password(pwd))
