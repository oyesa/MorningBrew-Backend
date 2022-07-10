from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from mzaziauth.models import CustomUser

User = get_user_model()

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    image = CloudinaryField('image',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def get_user(self):
        return{"username":self.user.username}

    def save_service(self):
        self.save

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    image = CloudinaryField('image',null=True)
    # comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='comment',null=True)

    def save_post(self):
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=500,blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey(Post, related_name = "comment", on_delete=models.CASCADE,default='')
    


    def save_comment(self):
        self.save()

class Group(models.Model):
   
    class Category(models.TextChoices):
        WELLBEING='WELLBEING','wellbeing'
        SINGLEPARENTWITHCHILDRENWITHADDITIONALNEEDS='SINGLEPARENTWITHCHILDRENWITHADDITIONALNEEDS(CAN)','singleparentwithchildrenwithadditionalneeds(can)'
        SINGLEPARENTFATHERS='SINGLEPARENTFATHERS','singleparentfathers'
    
    image = CloudinaryField('image',null=True)
    description = models.TextField()
    categories = models.CharField(choices=Category.choices, max_length=200,null=False, blank=False,default="")


    def save_group(self):
        self.save()

class Testimonials(models.Model):
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField()
    date_posted =  models.DateField(auto_now_add=True)

    def save_group(self):
        self.save()