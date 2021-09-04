from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return str(self.username)

class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    state = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.name