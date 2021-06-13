from django import forms

from django.forms import ModelForm
from .models import Hereglegch #, HereglegchRole

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name hhaa', max_length=100)
    # your_name1 = forms.IntegerField(label='Your name int')
    # message = forms.CharField(widget=forms.Textarea)
    # your_name3 = forms.CharField(label='Your name hhaa3', max_length=100)
    err_msg = forms.HiddenInput()

class HereglegchForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
         model = Hereglegch
         fields = ['ovog', 'ner', 'role', 'company', 'password']