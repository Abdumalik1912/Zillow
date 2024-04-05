from django import forms

class HomeSearchForm(forms.Form):
    city = forms.CharField(required=False)
    owner = forms.CharField(required=False)
    price = forms.DecimalField(required=False)