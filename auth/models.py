from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
     def create_user(self, email, password, **extra_fields):
          if not email:
               raise ValueError('The Email must be set')
          email = self.normalize_email(email)
          user = self.model(email=email, **extra_fields)
          user.set_password(password)
          user.save()
          return user


class UserProfile(AbstractBaseUser):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.EmailField(max_length=80, unique=True)
     wallet = models.IntegerField(default=0)
     phone_number = models.CharField(unique=True, max_length=11)
     account_number = models.CharField(max_length=15, unique=True, default='0211342')
     createdAt = models.DateTimeField(auto_now_add=True)
     is_staff = models.BooleanField(default=False)
     
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number', 'account_number']
     
     def __str__(self) -> str:
          return (f'{self.first_name} {self.last_name}')