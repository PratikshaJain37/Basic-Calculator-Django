from django import forms

from .models import Calculation

Operator_Choices =( 
    ("+", "Add"), 
    ("-", "Subtract"), 
    ("*", "Multiply"), 
    ("/", "Divide"),  
    ("!", "Find Factorial"),
    ("%", "Find percentage"),  
    ("**", "Find exponent"),
    ("//", "Find quotient and remainder"),
) 

class RawForm(forms.Form):
    number1 = forms.FloatField(max_value=1000000000, min_value=-1000000000)
    number2 = forms.FloatField(max_value=1000000000, min_value=-1000000000, required=False)
    operator = forms.ChoiceField(choices = Operator_Choices, widget=forms.RadioSelect)
    
