import random
import math
 
prime = set()
 
public_key = None
private_key = None
n = None
 
def primefiller():
    seive = [True] * 250
    seive[0] = False
    seive[1] = False
    for i in range(2, 250):
        for j in range(i * 2, 250, i):
            seive[j] = False
 
    for i in range(len(seive)):
        if seive[i]:
            prime.add(i)
 
 
def pickrandomprime():
    global prime
    k = random.randint(0, len(prime) - 1)
    it = iter(prime)
    for _ in range(k):
        next(it)
 
    ret = next(it)
    prime.remove(ret)
    return ret
 
 
def setkeys():
    global public_key, private_key, n
    prime1 = pickrandomprime()  
    prime2 = pickrandomprime()  
 
    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)
 
    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1
 
    public_key = e
 
    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1
 
    private_key = d

 
 
def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text
 
 
def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= n
        d -= 1
    return decrypted
 
 

def encoder(message):
    encoded_string = ""
    for char in message:
        if char.isdigit():  # Check if character is a digit
            encrypted_value = encrypt(int(char))  # Encrypt each character
            encoded_string += str(encrypted_value) + ","  # Append to string with comma delimiter
        else:
            encrypted_value = encrypt(ord(char))  # Encrypt each character
            encoded_string += str(encrypted_value) + ","  # Append to string with comma delimiter
    return encoded_string[:-1] 
 
 
def decoder(encoded):
    s = ''
    for num in encoded:
        s += chr(decrypt(num))
    return s

#from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#from cryptography.hazmat.backends import default_backend
#import os

#def encrypt(data, key):
    #iv = os.urandom(16)  # Initialization vector
    #cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    #encryptor = cipher.encryptor()
    #ciphertext = encryptor.update(data) + encryptor.finalize()
    #return iv + ciphertext + encryptor.tag

#def decrypt(encrypted_data, key):
    #iv = encrypted_data[:16]
    #tag = encrypted_data[-16:]
    #ciphertext = encrypted_data[16:-16]
    #cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    #decryptor = cipher.decryptor()
    #decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    #return decrypted_data

""" import bcrypt
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad """

# def generate_key(password):
#     try:
#         if len(password) == 0:
#             raise ValueError("Password cannot be empty")
#         password = hashlib.sha256(password.encode()).digest()
#         salt = bcrypt.gensalt()
#         key = bcrypt.kdf(password, salt, desired_key_bytes=32, rounds=100000)
#         return key
#     except ValueError as ve:
#         print(f"ValueError: {ve}")
#         return None
#     except bcrypt.BCryptError as be:
#         print(f"BCryptError: {be}")
#         return None
#     except Exception as e:
#         print(f"Error generating key: {e}")
#         return None

""" class AESCipher:
    def __init__(self, key):
        # self.key = generate_key(key)
        self.key = hashlib.sha256(key.encode()).digest()
    pass """

# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
# from base64 import urlsafe_b64encode, urlsafe_b64decode

# def encrypt_data(key, data):
#     cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
#     encryptor = cipher.encryptor()
#     encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
#     return urlsafe_b64encode(encrypted_data).decode()

#def decrypt_data(key, encrypted_data):
#    encrypted_data = urlsafe_b64decode(encrypted_data.encode())
#    cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
#    decryptor = cipher.decryptor()
#    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
#    return decrypted_data.decode()