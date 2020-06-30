from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculation
from .forms import RawForm
from .helpers import Calculate_Result
from django.utils import timezone

# Create your views here.

def home_view(request, *args, **kwargs):
    form = RawForm()
    context = {
        "form":form
    }
    return render(request, "home.html", context)

def result_view(request, *args, **kwargs):
    form = RawForm(request.GET)
    if request.method == "POST":
        form = RawForm(request.POST)
        if form.is_valid():

            # Setting up values
            number1=request.POST.get('number1')
            number2=request.POST.get('number2')
            operator=request.POST.get('operator')
            result = Calculate_Result(number1, number2, operator)
            asked_time = timezone.now()

            
            if result != 'invalid':
                # Creating object in database
                Calculation.objects.create(number1=number1, number2=number2, operator=operator, result=result, asked_time=asked_time)
                error = None
            
            else:
                error = 'Operator is invalid'

        else:
            print(form.errors)
            error = 'Number(s) is/are invalid'
            
        # Saving the last id
        last_id = Calculation.objects.last().id

        # Filtering only the last 5
        prev_objects = Calculation.objects.filter(id__gt=last_id-5)

        # Deleting all previous ones, so that max 5 can remain at a time
        Calculation.objects.filter(id__lt=last_id-4).delete()

        context = {
            "prev_objects": prev_objects,
            "error": error
        }
    
    return render(request, "result.html", context)
