def generate_key():
"""Generate a key for encryption."""
return Fernet.generate_key()
def encrypt_message(message, key):
"""Encrypt a message using the provided key."""
f = Fernet(key)
encrypted_message = f.encrypt(message.encode())
return encrypted_message
def decrypt_message(encrypted_message, key):
"""Decrypt an encrypted message using the provided key."""
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message)
return decrypted_message.decode()