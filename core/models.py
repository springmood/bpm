from django.db import models
from django.contrib.auth.models import User
import bcrypt


class Project(models.Model):
    title = models.CharField(max_length=225)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=225)
    desc = models.TextField()
    type = models.CharField(max_length=225, null=True)


class ProjectMember(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TaskMember(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TaskMember(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class User(models.Model):
    fname = models.CharField(max_length=225)
    lname = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)

    def set_password(self, password):
        bytes = password.encode('utf-8')
        # generating the salt
        salt = bcrypt.gensalt()
        # hashing the password
        hash = bcrypt.hashpw(bytes, salt)
        self.password = hash


class Role(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.title
