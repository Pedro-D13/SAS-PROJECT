from django.urls import path
from .views import PostListVIew

from . import views

app_name ="blog"
urlpatterns = [
    path('', PostListVIew.as_view(), name ='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('gallery/', views.gallery, name='blog_gallery'),
]
