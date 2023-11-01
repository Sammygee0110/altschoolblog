from django.shortcuts import render
from .models import Blog

# Create your views here.

blogs = Blog.objects.all()

def home(request):
    context = {"blogs":blogs}
    return render(request, "home.html", context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {'blog':blog}
    return render(request, "blog.html", context)