from rest_framework import serializers
from .models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'content', 'created_at', 'user']

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'email': obj.user.email,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name
        }
