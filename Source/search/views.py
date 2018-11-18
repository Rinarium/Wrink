from django.shortcuts import render
from home.views import check_authentication as authenticated
from django.contrib.auth.models import User
from post.models import Post


def search_page(request):
    context = authenticated(request)
    if 'search' in request.GET:
        search = request.GET.get('search')
        context['users'] = User.objects.filter(username__search=search)
        context['posts'] = Post.objects.filter(title__search=search)
    return render(request, 'search/search_page.html', context)
