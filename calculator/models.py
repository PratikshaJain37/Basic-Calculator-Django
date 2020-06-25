from django.db import models

# Create your models here.

class Numbers(models.Model):
    user_number1_text = models.FloatField()
    user_number2_text = models.FloatField()
    done_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_number_text

class Operation(models.Model):
    user_numbers = models.ManyToManyField(Numbers)
    operator_text = models.CharField(editable=False) 
    result_number = models.FloatField()

    def __str__(self):
        return self.operator_text
    