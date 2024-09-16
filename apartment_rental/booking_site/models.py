from django.db import models
from django.contrib.auth.models import User

class Subscribe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class SearchAvailability(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.IntegerField(default=0)
    kids = models.IntegerField(default=0)
    
    
    
class Apartment(models.Model):
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9,decimal_places=6, default=0)
    lng = models.DecimalField(max_digits=9,decimal_places=6, default=0)
    email = models.EmailField()
    price = models.IntegerField(default=0)
    max_people = models.PositiveSmallIntegerField(default=0)
    bathrooms = models.PositiveSmallIntegerField(default=0)
    bedrooms = models.PositiveSmallIntegerField(default=0)
    check_in = models.CharField(max_length=10)
    check_out = models.CharField(max_length=10)
    shower = models.CharField(max_length=50)
    wifi = models.CharField(max_length=50)
    tv = models.CharField(max_length=50)
    kitchen = models.CharField(max_length=50)
    heating = models.CharField(max_length=50)
    accessible = models.CharField(max_length=50)
    extra_info = models.TextField(max_length=100)
    rules = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}"
    


class UserProfileInfo(models.Model):
    
    #Adding more attributes to original class User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Additional
    portfolio_site = models.URLField(blank=True)
    
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    

    def __str__(self):
        return self.user.username