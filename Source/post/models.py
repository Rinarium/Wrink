from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from froala_editor.fields import FroalaField
from user_profile.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = FroalaField(theme='dark')
    date = models.DateField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voters = models.ManyToManyField(Profile)
    likes = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('post_page', kwargs={'post_id': self.id})


class Comment(models.Model):
    text = models.TextField(max_length=1000, blank=True)
    date = models.DateField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voters = models.ManyToManyField(Profile)
    likes = models.IntegerField(default=0, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
