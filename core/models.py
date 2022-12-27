from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title=models.CharField(max_length=225)
    desc=models.TextField()
    def __str__(self) -> str:
        return self.title

class Task(models.Model):
    title=models.CharField(max_length=225)
    desc=models.TextField()
    type=models.CharField(max_length=225, null=True)

class ProjectMember(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TaskMember(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)