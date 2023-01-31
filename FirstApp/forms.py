from django import forms
from FirstApp.models import *

class imageform(forms.ModelForm):
    class Meta:
        model= productImageModel
        fields = '__all__'