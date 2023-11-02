from django.db import models
from django.contrib import auth

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, default="lastname")

    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    topic = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.topic
class Blog(models.Model):
    title = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self) -> str:
        return self.title.topic