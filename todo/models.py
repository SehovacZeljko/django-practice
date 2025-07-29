from django.conf import settings
from django.db import models

# Create your models here.


class ToDoItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
