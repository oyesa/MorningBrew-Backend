from xml.etree.ElementTree import Comment
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

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    image = CloudinaryField('image', default='image')
    # comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='comment',null=True)

    def save_post(self):
        self.save()

    def __str__(self):
        return self.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey(Post, related_name = "comment", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.comment} Post'