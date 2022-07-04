from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    image = CloudinaryField('image',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField()

    def save_service(self):
        self.save

    def __str__(self):
        return self.title