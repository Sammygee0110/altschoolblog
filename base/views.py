from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

blogs = Blog.objects.all()

def home(request):
    blogcount = Blog.objects.count()
    context = {"blogs":blogs, "blogcount":blogcount}
    return render(request, "home.html", context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {'blog':blog}
    return render(request, "blog.html", context)

@login_required(login_url="home")
def createBlog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect("home")
    return render(request, "create_blog.html", {"form":form})

@login_required(login_url="home")
def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, 'create_blog.html', {"form":form})

@login_required(login_url="home")
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect("home")
    return render(request, "delete_blog.html")

def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User not found")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Incorrect Username or Password")

    return render(request, "login_register.html", {"page":page})

def registerPage(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect("login")
        else:
            messages.error(request, "An error occured")
    return render(request, "login_register.html", {"form":form})

def logoutUser(request):
    logout(request)
    return redirect("home")