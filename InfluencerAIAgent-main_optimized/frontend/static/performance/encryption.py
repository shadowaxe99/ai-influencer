class EncryptionService:
def __init__(self):
self.key = Fernet.generate_key()
self.cipher_suite = Fernet(self.key)
def encrypt_data(self, data):
cipher_text = self.cipher_suite.encrypt(data.encode())
return cipher_text
def decrypt_data(self, cipher_text):
plain_text = self.cipher_suite.decrypt(cipher_text)
return plain_text.decode()
encryption_service = EncryptionService()
encrypted_user_profile = encryption_service.encrypt_data(userProfile)
```