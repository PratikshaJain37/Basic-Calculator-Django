from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home_View(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

def Result_View(request, *args, **kwargs):
    return HttpResponse("<h1> This is the result page </h1>")