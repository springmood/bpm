from django.db import models
from user.models import User
from role.models import Role


class Project(models.Model):
    title = models.CharField(max_length=225)
    desc = models.TextField()
    slug = models.TextField(default=0)
    img = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.title


class ProjectMember(models.Model):
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
