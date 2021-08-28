from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    profile_info = models.TextField(max_length=50, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    favorites = models.ManyToManyField(Post)

    def __str__(self):
        return self.user
