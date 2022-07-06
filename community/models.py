from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Community(models.Model):
    
    class Category(models.TextChoices):
        SHAREYOUREXPERIENCE='SHAREYOUREXPERIENCE','Shareyourexperience'
        JOINAMZAZISPACEEVENT='JOINAMZAZISPACEEVENT','Joinmzazispaceevent'
        SUPPORTANDSERVICES='SUPPORTANDSERVICES','Supportandservices'
        SINGLEPARENTGROUPS='SINGLEPARENTGROUPS','Singleparentgroups'
        
    
    image = CloudinaryField('image', default='image')
    description = models.TextField(blank=True, max_length=300)
    categories = models.CharField(choices=Category.choices, max_length=200,null=False, blank=False,default="")


    def save_community(self):
        self.save()


    def __str__(self):
       return self.categories

    def create_community(self):
        """
        A method that creates a community
        """
        self.save()

class Hood(models.Model):
    name = models.CharField(max_length=100,blank=True)
    location= models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, max_length=300)

    def save_hood(self):
        self.save()


    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200,blank=True)
    image= CloudinaryField('image' , default='image')
    description = models.TextField(blank=True, max_length=300)
    date = models.DateField(auto_now_add=True, null=True)

    def save_event(self):
        self.save()


    def __str__(self):
        return self.title





 



