from django import forms
from core.models import Project, Task, User, Role,ProjectMember

# create a form


class ProjectForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Project
        # specity fields to be used
        fields = "__all__"
        # fields=('id','title','desc')
        # fields={
        #     "title",
        #     'desc'
        # }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"

class ProjectMemberForm(forms.ModelForm):
    class Meta:
        model=ProjectMember
        fields="__all__"