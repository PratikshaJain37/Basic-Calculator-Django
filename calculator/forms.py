from django import forms

from .models import Calculation

Operator_Choices =( 
    ("+", "Add"), 
    ("-", "Subtract"), 
    ("*", "Multiply"), 
    ("/", "Divide"),  
) 

class RawForm(forms.Form):
    number1 = forms.FloatField(label='Number 1', widget=forms.TextInput(attrs={"placeholder": "Number 1"}))
    number2 = forms.FloatField()
    operator = forms.ChoiceField(choices = Operator_Choices, widget=forms.RadioSelect)
    