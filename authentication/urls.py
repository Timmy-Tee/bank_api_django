from django.urls import path
from . views import Registration

urlpatterns = [
     path('registration', Registration, name='registration')
]