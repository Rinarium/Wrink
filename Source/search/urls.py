from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.search_page, name='search_page'),
]