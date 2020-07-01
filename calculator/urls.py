from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from .views import home_view, result_view

urlpatterns = [
    path('', home_view, name='home'),
    path('result/', result_view, name='result'),

]
