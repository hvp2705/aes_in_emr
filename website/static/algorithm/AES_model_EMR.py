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

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

def encrypt_data(key, data):
    cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
    return urlsafe_b64encode(encrypted_data).decode()

def decrypt_data(key, encrypted_data):
    encrypted_data = urlsafe_b64decode(encrypted_data.encode())
    cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data.decode()
