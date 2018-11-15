from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<profile_id>\d+)$', views.profile_page, name='profile_page'),
]
