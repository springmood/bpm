from django import forms
from core.models import Project,Task

# create a form 
class ProjectForm(forms.ModelForm):
    # create meta class 
    class Meta:
        # specify model to be used
        model=Project
        # specity fields to be used
        fields="__all__"
        # fields=('id','title','desc')
        # fields={
        #     "title",
        #     'desc'
        # }

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"
