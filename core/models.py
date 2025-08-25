from django.db import models

# Create your models here.
class Emp(models.Model):
  
  emp_name = models.CharField(max_length=60)
  emp_id = models.IntegerField()
  city = models.CharField(max_length=100)
