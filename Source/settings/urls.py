from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.settings_page, name='settings_page'),
]
