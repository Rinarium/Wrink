from django.shortcuts import render
from home.views import check_authentication as authenticated
from . import models


def profile_page(request, profile_id):
    return render(request, 'profile/profile_page.html', authenticated(request))
