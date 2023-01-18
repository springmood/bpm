from django.db import models

class Role(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.title