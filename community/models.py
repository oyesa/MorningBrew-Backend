from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Community(models.Model):
    CATEGORY =(
        ('share your experience','share your experience'),
        ('Join a mzazi space event','Join a mzazi space event'),
        ('Support and Services','Support and Services'),
        ('Single parent Groups','Single parent Groups'),
        
    )
    
    image = CloudinaryField('image', default='image')
    description = models.TextField(blank=True, max_length=300)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)

class Hood(models.Model):
    name = models.CharField(max_length=100,blank=True)
    location= models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, max_length=300)


    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200,blank=True)
    image= CloudinaryField('image' , default='image')
    description = models.TextField(blank=True, max_length=300)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_event(self):
        self.save()





 



