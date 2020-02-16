from django.db import models
from hotels.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save 

# Create your models here.
class hotels(models.Model):
    slug=models.SlugField(blank=True, unique=True)
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

    def get_absolute_url(self):
        return "view/{slug}/".format(slug=self.slug)

   


def hotel_pre_save_reciever(sender, instance ,*args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)     
pre_save.connect(hotel_pre_save_reciever,sender=hotels)