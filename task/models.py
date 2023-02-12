from django.db import models
from project.models import Project
import uuid
from django.utils import timezone

class Task(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=225)
    desc = models.TextField(null=True,blank=True) #blank means we are allowed to sub,it a form with this value being empty
    type = models.CharField(max_length=225, null=True,blank=True)
    state=models.CharField(max_length=200,null=True,blank=True)
    project_id = models.ForeignKey(Project,related_name='project', on_delete=models.CASCADE)
    created=models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
