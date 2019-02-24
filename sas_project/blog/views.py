from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView)
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def gallery(request):
    return render(request, 'blog/gallery.html')


def about(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/about.html', context)
