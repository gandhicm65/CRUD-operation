from django.db import models

# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Contact = models.CharField(max_length=30)
    Location = models.CharField(max_length=30)
    