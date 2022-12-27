from django import forms
from core.models import Project

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
