from django.db import models

# Create your models here.
class hotels(models.Model):
    city=models.CharField(max_length=30)
    price=models.FloatField()
    street=models.CharField(max_length=200)
    latitude=models.CharField(max_length=30)
    longitude=models.CharField(max_length=30)
    ratings=models.FloatField()
    hotel_title=models.CharField(max_length=50)
    image=models.CharField(max_length=200)

    def __str__(self):
        return self.city+"-"+self.hotel_title