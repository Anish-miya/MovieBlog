from django import forms
from .models import Newslatter


class joinform(forms.ModelForm):
    class Meta:
        model = Newslatter
        fields = ['email']