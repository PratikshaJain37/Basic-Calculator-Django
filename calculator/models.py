from django.db import models

# Create your models here.

class Calculation(models.Model):
    number1 = models.FloatField(default=1)
    number2 = models.FloatField(default=2)
    operator = models.TextField(default='+')
    result = models.FloatField(default=3)