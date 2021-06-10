from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name hhaa', max_length=100)
    # your_name1 = forms.IntegerField(label='Your name int')
    # message = forms.CharField(widget=forms.Textarea)
    # your_name3 = forms.CharField(label='Your name hhaa3', max_length=100)
    err_msg = forms.HiddenInput()

