from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

blogs = Blog.objects.all()

def home(request):
    context = {"blogs":blogs}
    return render(request, "home.html", context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {'blog':blog}
    return render(request, "blog.html", context)

def createBlog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "create_blog.html", {"form":form})

def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, 'create_blog.html', {"form":form})

def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect("home")
    return render(request, "delete_blog.html")