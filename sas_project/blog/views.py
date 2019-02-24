from django.shortcuts import render

from django.http import HttpResponse

from .models import Post
# Create your views here.

def home(request):
    context = { 'posts':Post.objects.all()[:3:-1] }
    return render(request, 'blog/home.html', context)

def gallery(request):
    return render(request, 'blog/gallery.html')

def about(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/about.html', context)
