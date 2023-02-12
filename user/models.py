from django.db import models
import bcrypt
import uuid
from django.utils import timezone


class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    first_name = models.CharField(max_length=225,null=True,blank=True)
    last_name = models.CharField(max_length=225,null=True,blank=True)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    username = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)

    def set_password(self, password):
        bytes = password.encode('utf-8')
        # generating the salt
        salt = bcrypt.gensalt()
        # hashing the password
        hash = bcrypt.hashpw(bytes, salt)
        self.password = hash
