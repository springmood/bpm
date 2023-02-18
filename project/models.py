from django.db import models
from user.models import User
from role.models import Role
import uuid
from django.utils import timezone


class Project(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=225)
    desc = models.TextField(null=True,blank=True)
    slug = models.TextField(default=0,blank=True)
    img = models.CharField(max_length=500, null=True,blank=True)
    created=models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.title


class ProjectMember(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
   