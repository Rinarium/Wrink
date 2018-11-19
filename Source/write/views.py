from django.shortcuts import render, redirect
from home.views import check_authentication as authenticated
from post.models import Post
import datetime


def write_page(request):
    if not request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        title = request.POST.get('title')
        if not title:
            title = 'Null'
        post = Post.objects.create(title=title, body=request.POST.get('body'),
                                   date=datetime.date.today(), author=request.user)
        post.save()
        context = authenticated(request)
        context['post'] = post
        return redirect('post_page', post.id)
    return render(request, 'write/write_page.html', authenticated(request))
