from django.db import models

# Create your models here.
class airlines(models.Model):
    airlines_name=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    departure_time=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.airlines_name+" "+self.source+"-"+self.destination

    def cutprice(self):
        return self.price+(self.price*0.1)

    def depart_time(self):
        
        f=int(self.departure_time/100)
        l=int(self.departure_time%100)
        f=str(f)
        if(l==0):
            l="00"
        else:
            l=str(l)
        if (self.departure_time <1200):
            return f+":"+l+" "+"a.m"
        else:
            return f+":"+l+" "+"p.m"

def nametest(self):
    return self.airlines_name