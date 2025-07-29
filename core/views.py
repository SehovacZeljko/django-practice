from django.shortcuts import render
from rest_framework import viewsets
from core.models import User
from core.serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):  # or ModelViewSet if needed
    queryset = User.objects.all()
    serializer_class = UserSerializer
