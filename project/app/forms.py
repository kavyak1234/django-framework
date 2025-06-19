from django import forms
from .models import *

class student_Normal_form(forms.Form):
    roll = forms.IntegerField()
    name = forms.CharField()
    age = forms.IntegerField()

class ModelForm(forms.ModelForm):
    class Meta:
        model = samplestudent
        fields = '__all__'