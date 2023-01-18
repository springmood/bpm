from django import forms
from user.models import User

class Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

