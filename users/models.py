from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null = True)
    username = models.CharField(max_length=100, blank=True, null = True)
    location = models.CharField(max_length=100, blank=True, null = True)
    email = models.EmailField(max_length=100, blank=True, null = True)
    caption = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=100, blank=True, null = True)
    social_twitter = models.CharField(max_length=100, blank=True, null = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null = True)
    description = models.CharField(max_length=200, blank=True, null = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

