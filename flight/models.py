from django.db import models

# Create your models here.
class airlines(models.Model):
    airlines_name=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    departure_time=models.IntegerField()
    price=models.IntegerField()