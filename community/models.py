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




