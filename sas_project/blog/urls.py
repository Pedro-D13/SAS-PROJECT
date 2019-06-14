from django.urls import path
from .views import (BaseTemplate,
                    PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostAllView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    EventListView,
                    EventDetailView)
# EventCreateView)
from . import views

app_name = "blog"
urlpatterns = [
    path('', BaseTemplate.as_view(), name='post_home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/blog/', PostAllView.as_view(), name="post_all"),
    path('events/', EventListView.as_view(), name="event_list"),
    path('events/<int:pk>/', EventDetailView.as_view(), name="event_list"),
    path('about/', views.about, name='blog_about'),
    path('gallery/', views.gallery, name='blog_gallery'),
]
