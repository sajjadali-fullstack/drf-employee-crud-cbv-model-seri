from django.db import models

# Create your models here.

class Employee(models.Model):
    # emp_name, emp_sal, emp_add
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=450) 
    emp_sal = models.FloatField()
    emp_add = models.CharField(max_length=950)