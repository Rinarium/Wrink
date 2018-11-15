from django.shortcuts import render
from home.views import check_authentication as authenticated
from post.models import Post
import datetime


def write_page(request):
    if request.method == 'POST':
        post = Post.objects.create(title=request.POST.get('title'), body=request.POST.get('body'),
                                   date=datetime.date.today(), author=request.user)
        post.save()
        context = authenticated(request)
        context['post'] = post
        return render(request, 'post/post_page.html', context)
    return render(request, 'write/write_page.html', authenticated(request))
