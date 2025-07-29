
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import ToDoItem
from .serializers import ToDoItemSerializer


# Create your views here.

# class ToDoItemViewSet(ModelViewSet):
#     queryset = ToDoItem.objects.all()
#     serializer_class = ToDoItemSerializer


class ToDoItemViewSet(ModelViewSet):
    serializer_class = ToDoItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return only the current user's todo items"""
        return ToDoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically set the user when creating a new todo item"""
        serializer.save(user=self.request.user)
