from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password



class UserSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
     class Meta:
          model: UserProfile
          fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']
          extra_kwargs = {
               'password': {'write_only': True},
               'first_name': {'required': True},
               'last_name': {'required': True}
          }