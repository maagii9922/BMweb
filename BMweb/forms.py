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
        fields = ['ovog', 'ner','mail', 'role','state', 'company', 'password','reg_date']

class ProductForm(ModelForm):
    borBoloh = forms.BooleanField(required=False, initial=True)
    hudAwch = forms.BooleanField(required=False, initial=True)
    zarBoloh = forms.BooleanField(required=False, initial=True)
    # company = forms.ModelMultipleChoiceField(queryset=Company.objects.all(),widget=forms.CheckboxSelectMultiple)

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
            'zarBoloh',
            'state',
            ]