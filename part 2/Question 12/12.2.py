import hashlib
from Crypto.Cipher import AES
from base64 import b64encode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        counter = self.block_size.to_bytes(self.block_size, "big")
        cipher = AES.new(self.key, AES.MODE_CTR, counter=lambda: counter)
        # FIX ME: encrypted_text = ?
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(counter + encrypted_text).decode("utf-8")

    def __pad(self, plain_text):
        pad_len = self.block_size - len(plain_text) % self.block_size
        return plain_text + chr(pad_len) * pad_len

if __name__ == '__main__':
    msg = input("Enter message: ")
    cipher = AESCipher("another_key")
    print(cipher.encrypt(msg))
