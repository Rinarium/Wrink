from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.write_page, name='write_page'),
]
