from django import forms
from task.models import Task


class Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


# Serializers define the API representation.
class UploadFileForm(forms.Form):
    file=forms.FileField()