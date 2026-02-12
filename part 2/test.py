import hashlib

def secure_hash(text):
    # TODO
    encoded = text.encode()
    h = hashlib.sha3_256()
    h.update(encoded)
    
    return encoded.hexdigest
print(secure_hash("HelloWorld"))
