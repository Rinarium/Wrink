from django.shortcuts import render, redirect
from home.views import check_authentication as authenticated


def settings_page(request):
    if not request.user.is_authenticated:
        return redirect('home_page')
    return render(request, 'settings/settings_page.html', authenticated(request))
