from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="member.png", upload_to="profile_pics")
    role = models.TextField(max_length=500, blank=True, default="SOSA Member")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
