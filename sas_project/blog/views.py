from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostListVIew(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

def gallery(request):
    return render(request, 'blog/gallery.html')

def about(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/about.html', context)
