from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManger(BaseUserManager):
     def create_user(self, email, password=None, **extra_fields):
          if not email:
               raise ValueError("Please Input Your Email")
          email = self.normalize_email(email)
          extra_fields.setdefault('is_active', True) 
          user = self.model(email=email, **extra_fields)
          user.set_password(password)
          user.save()
          return user
     
     def create_superuser(self, email, password, **extra_fields):
          extra_fields.setdefault('is_staff', True)
          extra_fields.setdefault('is_superuser', True)
          extra_fields.setdefault('is_verified', True)
          
          if extra_fields.get('is_staff') is not True:
               raise ValueError(f'Super User must have is_staff = True')
          if extra_fields.get('is_superuser') is not True:
               raise ValueError(f'Super User must have is_superuser = True')
          return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.CharField(unique=True, max_length=255)
     wallet = models.BigIntegerField(default=0)
     account_number = models.CharField(max_length=255)
     is_staff = models.BooleanField(default=False)
     is_superuser = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
     is_verified = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
     
     objects = UserManger()
     USERNAME_FIELD = "email"
     
     def __str__(self):
          return (f'{self.email}')