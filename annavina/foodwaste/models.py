from django.db import models
from geopy.geocoders import Nominatim
from django.contrib.auth.models import AbstractUser


class foodmart(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    pincode=models.CharField(max_length=10)
    lat=models.CharField(max_length=20,null=True,blank=True)
    lon=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=100,null=False,blank=False)
    phone_number = models.CharField(max_length=12)
    quantity= models.CharField(max_length=12)
    
    
    def save(self,*args, **kwargs):
        geolocator = Nominatim(user_agent="foodwaste")
        location = geolocator.geocode(int(self.pincode))
        self.lat=location.latitude
        self.lon=location.longitude
        super(foodmart,self).save(*args,**kwargs)    
    def __str__(self):
        return self.name

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_customer = models.BooleanField('Is customer', default=False)