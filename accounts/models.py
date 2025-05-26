from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
import pycountry
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,user_name,phone, email,country,password=None):
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
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,user_name,phone, email,country,password=None):
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


class Account(AbstractBaseUser):
    @staticmethod
    def get_country():
        countries = list(pycountry.countries)
        country_choices = [ (country.alpha_2  ,country.name) for country in countries]
        return country_choices
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100,unique=True)
    user_name = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=2,choices=get_country(), default='MA')
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.TimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.user_name
    
    def has_perm(self, perm , obj=None):
        return self.is_admin
    
    def has_module_perm(self, app_label):
        return True
    
            
        