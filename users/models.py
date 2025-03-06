from django.contrib.auth.models import AbstractUser
from django.db import models
from cryptography.fernet import Fernet
import os

# Generate and store encryption key
ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY', Fernet.generate_key())
cipher = Fernet(ENCRYPTION_KEY)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    encrypted_password = models.BinaryField()

    def set_encrypted_password(self, raw_password):
        self.encrypted_password = cipher.encrypt(raw_password.encode())

    def check_encrypted_password(self, raw_password):
        return cipher.decrypt(self.encrypted_password).decode() == raw_password
