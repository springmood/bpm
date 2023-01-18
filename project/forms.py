from django import forms
from project.models import Project,ProjectMember

class Form(forms.ModelForm):
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

class ProjectMemberForm(forms.ModelForm):
    class Meta:
        model=ProjectMember
        fields="__all__"