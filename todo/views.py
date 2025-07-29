
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from .models import ToDoItem
from .serializers import ToDoItemSerializer


# Create your views here.

class ToDoItemViewSet(ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
