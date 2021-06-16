from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

class Encode:
    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()
    pubKeyPEM = ''
    privKeyPEM = ''

    def __init__(self):
        self.pubKeyPEM = self.pubKey.exportKey()
        self.privKeyPEM = self.keyPair.exportKey()

    def encrypt(self, password):
        password = bytes(password, encoding='utf-8')
        encryptor = PKCS1_OAEP.new(self.pubKey)
        return encryptor.encrypt(password)

    def decrypt(self, password):
        decryptor = PKCS1_OAEP.new(self.keyPair)
        return decryptor.decrypt(password).decode('utf-8')

    def hash_password(self, password):
        return self.encrypt(password)

    def verify(self, hash, password):
        hash = self.decrypt(hash)
        return hash == password
