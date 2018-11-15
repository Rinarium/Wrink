from django.shortcuts import render
from home.views import check_authentication as authenticated


def post_page(request):
    return render(request, 'post/post_page.html', authenticated(request))
