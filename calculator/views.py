from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculation

# Create your views here.

def home_view(request, *args, **kwargs):
    obj = Calculation.objects.get(id=1)

    context = {
        "num1": obj.number1,
        "num2": obj.number2,
        "operator": obj.operator
    }
    return render(request, "home.html", context)

def result_view(request, *args, **kwargs):
    obj = Calculation.objects.get(id=1)
    context = {
        "num1": obj.number1,
        "num2": obj.number2,
        "operator": obj.operator,
        "result": obj.result
    }
    return render(request, "home.html", context)
