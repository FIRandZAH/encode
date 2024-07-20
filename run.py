from Crypto.Cipher import AES
import binascii
import os

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

encoded_file_path = '/storage/emulated/0/cadangan/penting/t.txt'

decryption_key_hex = os.getenv('DECRYPTION_KEY')
if decryption_key_hex is None:
    raise ValueError("Decryption key not found in environment variables")

decryption_key = binascii.unhexlify(decryption_key_hex)

encrypted = read_file(encoded_file_path)

iv = encrypted[:16]
encrypted_message = encrypted[16:]

cipher = AES.new(decryption_key, AES.MODE_CFB, iv)

decrypted = cipher.decrypt(encrypted_message)

exec(decrypted.decode('utf-8'))
