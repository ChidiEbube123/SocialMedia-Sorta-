from django.urls import path
from .views import post_home,create_post
urlpatterns = [
    path('',post_home, name="post_home"),
    path('make/', create_post, name="create_post")
]
