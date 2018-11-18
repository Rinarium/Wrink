from django.shortcuts import render
from home.views import check_authentication as authenticated
from django.contrib.auth.models import User
from post.models import Post


def search_page(request):
    context = authenticated(request)
    if 'search' in request.GET:
        search = request.GET.get('search')
        context['users'] = User.objects.filter(username__icontains=search)
        context['postsTitle'] = Post.objects.filter(title__icontains=search)
        context['postsBody'] = Post.objects.filter(body__icontains=search)
    return render(request, 'search/search_page.html', context)
