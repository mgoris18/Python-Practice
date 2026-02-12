import hashlib
from Crypto.Cipher import AES
from base64 import b64encode
import os

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = plain_text.encode()
        iv = os.urandom(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # FIX ME: encrypted_text = ?
        encrypted_text = cipher.encrypt(plain_text)
        return b64encode(iv + encrypted_text).decode("utf-8")

if __name__ == '__main__':
    msg = input("Enter message: ")
    cipher = AESCipher("cbc_key")
    print(cipher.encrypt(msg))
