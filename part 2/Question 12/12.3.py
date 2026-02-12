import hashlib
from Crypto.Cipher import AES
from base64 import b64encode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = plain_text.encode()
        counter = self.block_size.to_bytes(self.block_size, "big")
        cipher = AES.new(self.key, AES.MODE_CTR, counter=lambda: counter)
        # FIX ME: encrypted_text = ?
        encrypted_text = cipher.encrpt(plain_text)
        return b64encode(counter + encrypted_text).decode("utf-8")

if __name__ == '__main__':
    msg = input("Enter message: ")
    cipher = AESCipher("third_key")
    print(cipher.encrypt(msg))
