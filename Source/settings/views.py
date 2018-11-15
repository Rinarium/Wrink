from django.shortcuts import render
from home.views import check_authentication as authenticated


def settings_page(request):
    return render(request, 'settings/settings_page.html', authenticated(request))
