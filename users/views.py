from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer,UserSerializer

USER = get_user_model()

class CreateUserView(CreateAPIView):

    model = USER
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer

class UserView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = USER.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer