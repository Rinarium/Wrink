from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<post_id>\d+)$', views.post_page, name='post_page'),
]
