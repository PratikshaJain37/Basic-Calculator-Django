from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculation
from .forms import RawForm
from .helpers import help_calculate

# Create your views here.

def home_view(request, *args, **kwargs):
    form = RawForm()
    
    context = {
        "form":form
    }
    return render(request, "home.html", context)

def result_view(request, *args, **kwargs):
    form = RawForm()
    if request.method == "POST":
        form = RawForm(request.POST)
        if form.is_valid():
            number1=request.POST.get('number1')
            number2=request.POST.get('number2')
            operator=request.POST.get('operator')
            result = help_calculate(number1, number2, operator)
            
            Calculation.objects.create(number1 =number1, number2=number2, operator=operator, result=result)

        else:
            print(form.errors)
    objs = Calculation.objects.last()
    
    context = {
        "object": objs,

    }
    return render(request, "result.html", context)
