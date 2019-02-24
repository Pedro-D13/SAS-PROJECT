from django.urls import path
from .views import PostListView, PostDetailView , PostCreateView

from . import views

app_name ="blog"
urlpatterns = [
    path('', PostListView.as_view(), name ='post_home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/<int:pk>/', PostCreateView.as_view(), name="post_create"),
    path('about/', views.about, name='blog_about'),
    path('gallery/', views.gallery, name='blog_gallery'),
]
