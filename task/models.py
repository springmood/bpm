from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=225)
    desc = models.TextField()
    type = models.CharField(max_length=225, null=True)

    def __init__(self) -> str:
        return self.title
