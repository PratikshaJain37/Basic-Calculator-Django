from django.db import models
from django.utils import timezone
# Create your models here.

Operator_Choices =( 
    ("+", "Add"), 
    ("-", "Subtract"), 
    ("*", "Multiply"), 
    ("/", "Divide"),  
) 

class Calculation(models.Model):
    number1 = models.FloatField(default=0)
    number2 = models.FloatField(default=0)
    operator = models.CharField(max_length=2, choices = Operator_Choices, default = '+')
    result = models.CharField(max_length=200, default=0)
    asked_time = models.DateTimeField(default=timezone.now)

    

    def __str__(self): 
        # This makes the object refer to itself as asked_time rather than id
        return str(self.asked_time)