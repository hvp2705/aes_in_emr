from sympy import primerange
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, padding, hashes
import random
import math

class RSAEncryption:
    def __init__(self):
        self.prime = set()
        self.public_key = None
        self.private_key = None
        self.n = None

    def primefiller(self):
        self.prime.update(primerange(2, 250))

    def pickrandomprime(self):
        return self.prime.pop()

    def setkeys(self):
        prime1 = self.pickrandomprime()  
        prime2 = self.pickrandomprime()  

        self.n = prime1 * prime2
        fi = (prime1 - 1) * (prime2 - 1)

        e = math.gcd(fi, prime1 - 1) + 1
        self.public_key = e

        d = math.gcd(fi, prime2 - 1) + 1
        self.private_key = d

    def encrypt(self, message):
        e = self.public_key
        encrypted_text = pow(message, e, self.n)
        return encrypted_text

    def decrypt(self, encrypted_text):
        d = self.private_key
        decrypted = pow(encrypted_text, d, self.n)
        return decrypted

    def encoder(self, message):
        block_size = 16  # Set the block size
        encoded_string = ""
        for i in range(0, len(message), block_size):
            block = message[i:i+block_size]  # Get a block of characters
            encrypted_block = self.encrypt(int.from_bytes(block.encode(), 'big'))  # Encrypt the block
            encoded_string += str(encrypted_block) + ","  # Append to string with comma delimiter
        return encoded_string

    def decoder(self, encoded):
        block_size = 16  # Set the block size
        s = ''
        encoded_blocks = encoded.split(",")  # Split the encoded string into blocks
        for encoded_block in encoded_blocks:
            decrypted_block = self.decrypt(int(encoded_block))
            block = decrypted_block.to_bytes((decrypted_block.bit_length() + 7) // 8, 'big').decode()  # Convert decrypted block to string
            s += block
        return s

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

def encrypt(message):
    encrypted_text = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_text

def decrypt(encrypted_text):
    decrypted = private_key.decrypt(
        encrypted_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()