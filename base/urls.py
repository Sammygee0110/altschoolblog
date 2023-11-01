from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/<str:pk>", views.blog, name="blog"),
    path("create-blog/<str:pk>", views.updateBlog, name="create-blog"),
    path("delete-blog/<str:pk>", views.deleteBlog, name="delete-blog")
]