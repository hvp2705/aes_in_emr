from sympy import primerange
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
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

    def generate_keys(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def encrypt(self, message):
        ciphertext = self.public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode()

    def encoder(self, message):
        block_size = 16  # Set the block size
        encoded_string = ""
        for i in range(0, len(message), block_size):
            block = message[i:i + block_size]  # Get a block of characters
            block_bytes = block.encode()  # Convert block to bytes
            encrypted_block = self.encrypt(int.from_bytes(block_bytes, 'big'))  # Encrypt the block
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

