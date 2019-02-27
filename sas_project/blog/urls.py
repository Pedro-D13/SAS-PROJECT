from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostAllView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)
from . import views

app_name = "blog"
urlpatterns = [
    path('', PostListView.as_view(), name='post_home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/blog/', PostAllView.as_view(), name="post_all"),
    path('about/', views.about, name='blog_about'),
    path('gallery/', views.gallery, name='blog_gallery'),
]
