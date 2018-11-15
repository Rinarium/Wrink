from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    topics = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=300, blank=True)
    voters = models.ManyToManyField('self')
    likes = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('profile_page', kwargs={'profile_id': self.id})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
