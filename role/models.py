from django.db import models
import uuid
from django.utils import timezone

class Role(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=225)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
