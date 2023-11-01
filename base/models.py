from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    email = models.EmailField()
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    topic = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.topic
class Blog(models.Model):
    title = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title