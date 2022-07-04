import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        User = self.model(username=username, email=self.normalize_email(email), first_name=first_name)
        User.set_password(password)
        User.save()

        return User

    def create_superuser(self, username, email, password):
      if password is None:
          raise TypeError('Superusers must have a password.')

      user = self.create_user(username, email, password)
      user.is_superuser = True
      user.is_staff = True
      user.is_verified=True
      user.save()

      return user
