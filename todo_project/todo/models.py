from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

class User(AbstractUser):
    pass