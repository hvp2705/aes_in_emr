import bcrypt
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

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

class AESCipher:
    def __init__(self, key):
        # self.key = generate_key(key)
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, data):
        if isinstance(data, str):
            data = data.encode()
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = cipher.iv
        return iv, ct_bytes

    def decrypt(self, data):
        iv = data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        pt = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
        if isinstance(pt, bytes):
            return pt.decode()
        return pt

    def encrypt_file(self, file_name):
        chunk_size = 64 * 1024  # 64KB
        try:
            with open(file_name, 'rb') as fo:
                with open(file_name + ".enc", 'wb') as enc_file:
                    while True:
                        chunk = fo.read(chunk_size)
                        if not chunk:
                            break
                        enc_chunk = self.encrypt(chunk)
                        enc_file.write(enc_chunk[0] + enc_chunk[1])
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")

    def decrypt_file(self, file_name):
        chunk_size = 64 * 1024  # 64KB
        try:
            with open(file_name, 'rb') as enc_file:
                with open(file_name[:-4], 'wb') as dec_file:
                    while True:
                        enc_chunk = enc_file.read(chunk_size)
                        if not enc_chunk:
                            break
                        dec_chunk = self.decrypt(enc_chunk)
                        dec_file.write(dec_chunk)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")