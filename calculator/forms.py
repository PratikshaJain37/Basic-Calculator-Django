from django import forms

from .models import Calculation

class CalculationForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = [
            'number1', 
            'number2',
            'operator'
        ]

class RawForm(forms.Form):
    number1 = forms.FloatField()
    number2 = forms.FloatField()
    operator = forms.CharField()
