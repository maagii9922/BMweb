from django import forms

from django.forms import ModelForm, fields
from .models import Company, Hereglegch, Product ,ProdType ,Category  # , HereglegchRole

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['comName','hayag','phone']

class HereglegchForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hereglegch
        fields = ['ovog', 'ner', 'role', 'company', 'password']

class ProductForm(ModelForm):
    borBoloh = forms.BooleanField(required=False, initial=True)
    hudAwch = forms.BooleanField(required=False, initial=True)
    class Meta:
        model = Product
        fields = [
            'prodName',
            'zCode', 
            'prodType',
            'zzCode',
            'price', 
            'hemNegj',
            'hudNegj',
            'company', 
            'erNershil',
            'emHelber',
            'company',
            'paiz', 
            'uildwerlegch',
            'uNiiluulegch',
            'category',
            'borBoloh',
            'hudAwch',
            'state',]