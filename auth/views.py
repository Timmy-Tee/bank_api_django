from rest_framework import mixins, viewsets
from .serializers import UserSerializer

# Create your views here.
class RegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
     def create(self, request, *args, **kwargs):
          data = request.data
          print(data)