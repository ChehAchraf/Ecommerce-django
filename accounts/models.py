from django.db import models
from django.contrib.auth.models import BaseUserManager
import pycountry
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,user_name, email,country,password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have a password')
        if not user_name:
            raise ValueError('User must have a user name')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            country=country,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,user_name, email,country,password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            email=email,
            country=country,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user