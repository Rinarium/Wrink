from django.shortcuts import render
from home.views import check_authentication as authenticated
from django.core.exceptions import ObjectDoesNotExist
from .models import Post


def post_page(request, post_id):
    context = authenticated(request)
    try:
        context['post'] = Post.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        return render(request, 'home/home_page.html', context)
    return render(request, 'post/post_page.html', context)
