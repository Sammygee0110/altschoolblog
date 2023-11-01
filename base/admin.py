from django.contrib import admin
from .models import Blog, Topic, User

# Register your models here.

admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(User)