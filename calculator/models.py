from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Calculation(models.Model):
    number1 = models.FloatField(default=1)
    number2 = models.FloatField(default=2)
    operator = models.TextField(default='+')
    result = models.CharField(max_length=2, default=0)
    asked_time = models.DateTimeField(default=timezone.now)