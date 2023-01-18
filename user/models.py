from django.db import models
import bcrypt

class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    username=models.CharField(max_length=255)

    def set_password(self, password):
        bytes = password.encode('utf-8')
        # generating the salt
        salt = bcrypt.gensalt()
        # hashing the password
        hash = bcrypt.hashpw(bytes, salt)
        self.password = hash
