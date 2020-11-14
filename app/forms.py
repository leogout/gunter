from django import forms

from app.models import Category


class PurchaseForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.RadioSelect())
    price = forms.FloatField()
