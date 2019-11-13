from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    img = models.ImageField(
        blank=True, default="lotus.jpeg", upload_to="posts_bg")

    class Meta:
        ordering = ('date_posted',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    comment_date = models.DateTimeField(default=timezone.now)


class Event(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)
    img = models.ImageField(blank=True)

    class Meta:
        ordering = ('event_date',)

    def __str__(self):
        return f"{self.title}--{self.event_date}--{self.event_time}"
