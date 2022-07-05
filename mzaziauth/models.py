from re import L
from tokenize import Single
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField 
from cloudinary.models import CloudinaryField
from phonenumbers import CountryCodeSource



# Create your models here.
class CustomUserManager(BaseUserManager):
    

    def create_user(self, username, email,f_name,l_name,user_role, password=None):
        """Create and return a `customUser` with an email, username,first_name,last_name, and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        customUser = self.model(username=username, email=self.normalize_email(email) ,f_name=f_name,l_name=l_name,user_role=user_role)
        customUser.set_password(password)
        customUser.save()

        return customUser

    def create_superuser(self, username, email,password,**extra_fields):
      """
      Create and return a `customUser` with superuser powers.
      Superuser powers means that this use is an admin that can do anything
      they want.
      """
      if password is None:
          raise TypeError('Superusers must have a password.')

      customUser = self.create_user(username, email,password,**extra_fields)
      customUser.is_superuser = True
      customUser.is_staff = True
      customUser.is_verified=True
      customUser.save()

      return customUser
  
# class UserRole(models.Model):
    
#     CHOICES = [
#     ('SingleParent', 'SingleParent'),
#     ('Counsellor', 'Counsellor'),
#     ]

#     user_role = models.CharField( choices=CHOICES, max_length=30,null=False, blank=False)
    
#     def save_role(self):
#       self.save()
#     def __str__(self):
#       return self.user_role
  
class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    class Roles(models.TextChoices):
        SINGLEPARENT='SINGLEPARENT','SingleParent'
        COUNSELLOR='COUNSELLOR','Counsellor'
        
    username = models.CharField(db_index=True, max_length=255, unique=True)
    f_name = models.CharField(('First Name'), max_length=50, blank=True)
    l_name = models.CharField(('Last Name'), max_length=50, blank=True)
    
    user_role = models.CharField(choices=Roles.choices, max_length=30,null=False, blank=False)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
    def token(self):
        return self.generate_jwt_token()


       
    def generate_jwt_token(self):
        user_details = {'email':self.email,'username':self.username}
        token = jwt.encode(
            {
                'user_data':user_details,
                'exp':datetime.now() + timedelta(hours=24)
            },settings.SECRET_KEY,algorithm ='HS256'
        )
        
        return token

class Profile(models.Model):
    user = models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    prof_pic = CloudinaryField('images', default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.TextField(blank=True, max_length=255 ,default='please update your bio')
    phone = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.user

    def save_profile(self):
        '''Add Profile to database'''
        self.save()
   