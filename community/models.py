from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Community(models.Model):
    image = CloudinaryField('image', default='image')
    description = models.TextField(blank=True, max_length=300)
    category = models.CharField(max_length=100,default='category')



