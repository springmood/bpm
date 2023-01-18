from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=225)
    desc = models.TextField()
    img = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.title
