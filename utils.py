from django.conf import settings
from cryptography.fernet import Fernet
import base64

# Retrieve the encryption key from settings.py
ENCRYPTION_KEY = "NkJy6vpDHJVl7lda-RxHezopc7I_eVKDEwtu2-h_opE="

# Decode if necessary (Only do this if your key is in a string format)
key = ENCRYPTION_KEY.encode()  # Convert to bytes
cipher = Fernet(key)  # Initialize the cipher

def encrypt_data(plain_text):
    """Encrypts the given plain text."""
    return cipher.encrypt(plain_text.encode()).decode()



def decrypt_data(encrypted_text):
    try:
        print(f"Encrypted text received: {encrypted_text}")  # Debugging
        decrypted_bytes = cipher.decrypt(encrypted_text.encode())
        decrypted_text = decrypted_bytes.decode()
        print(f"Decrypted text: {decrypted_text}")  # Debugging
        return decrypted_text
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None