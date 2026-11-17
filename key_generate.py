from cryptography.fernet import Fernet


key = Fernet.generate_key()
print("Secret Key:", key.decode())  # Save this key securely
