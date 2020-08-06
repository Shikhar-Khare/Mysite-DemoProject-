from django.db import models

# Create your models here.
class teacher(models.Model):
    name: models.CharField(max_length=80)
    age: models.IntegerField

class student(models.Model):
    name: models.CharField(max_length=80)
    result = models.BooleanField(default=False)