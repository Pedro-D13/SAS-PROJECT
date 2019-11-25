import os
import json
from blog.forms import ContactForm
from django.views.generic.edit import FormView
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
from .models import Post, Event, Comment
from users.models import Profile
from django.core.mail import send_mail


class BaseTemplate(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 3


def homepageview(request, *args, **kwargs):
    posts = Post.objects.all().order_by('-date_posted')[:3]
    events = Event.objects.all().order_by('-event_date')[:3]
    staff = User.objects.filter(is_staff=True)
    context = {'posts': posts, 'events': events, 'staff': staff}
    return render(request, 'blog/base.html', context)


class PostListView(ListView):
    model = Post
    template_name = "blog2/blog_posts_list.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = "blog2/user_posts.html"
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
    model = Event
    template_name = "blog2/event_detail.html"
    context_object_name = "event"

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


class ContactView(FormView):
    template_name = ''
    form_class = ContactForm
    success_url = "blog2/success.html"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


# def contact_member(request):
#     if form.is_valid():
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']
#         sender = form.cleaned_data['sender']
#         cc_myself = form.cleaned_data['cc_myself']

#         recipients = ['info@example.com']
#         if cc_myself:
#             recipients.append(sender)

#         send_mail(subject, message, sender, recipients)
#         return HttpResponseRedirect('/thanks/')


class StaffProfileView(DetailView):
    model = User
    template_name = "blog2/staff_profile.html"
    context_object_name = "staff"

    def get_queryset(self):
        staff = User.objects.filter(is_staff=True)
        staff_profile = staff.filter(id=self.kwargs.get("pk"))
        return staff_profile


class CommentListView(ListView):
    model = Comment
    template_name = "blog2/postcomment.html"
    context_object_name = "comments"


# staff = User.objects.all().filter(is_staff="True")
# staff.profile.id
# profile1 = Profile.objects.get(id=user1.profile.id)
