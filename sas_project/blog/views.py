import os
import json
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post, Event


class BaseTemplate(ListView):
    model = Post
    template_name = "blog2/index.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 3


def homepageview(request, *args, **kwargs):
    posts = Post.objects.all().order_by('-date_posted')[:6]
    events = Event.objects.all().order_by('-event_date')[:3]
    context = {'posts': posts, 'events': events}
    return render(request, 'blog2/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = "blog2/blog_posts_list.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostAllView(ListView):
    model = Post
    template_name = "blog2/all_posts_list.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "blog2/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'img']
    template_name = "blog2/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'img']
    template_name = "blog2/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class EventListView(ListView):
    model = Event
    template_name = "blog2/event.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    pass

# class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     pass


def gallery(request):
    img_list = os.listdir("static/blog/img")
    for _ in img_list:
        if _ == ".DS_Store":
            img_list.remove(_)
    return render(request, 'blog2/gallery.html', {'img_list': img_list})


def about(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog2/about.html', context)
