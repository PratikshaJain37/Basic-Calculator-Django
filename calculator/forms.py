from django import forms

from .models import Calculation


class RawForm(forms.Form):
    number1 = forms.FloatField()
    number2 = forms.FloatField()
    operator = forms.CharField()
