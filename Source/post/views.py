from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import datetime
from home.views import check_authentication as authenticated
from .models import Post, Comment


def count_rating(post):
    try:
        rating = post.likes / post.voters.count()
    except ZeroDivisionError:
        rating = 1.0
    return rating


def post_page(request, post_id):
    context = authenticated(request)
    try:
        post = Post.objects.get(pk=post_id)
        context['post'] = post
    except ObjectDoesNotExist:
        return redirect('home_page')

    if request.method == 'POST' and 'comment' in request.POST:
        if request.POST.get('comment'):
            comment = Comment.objects.create(text=request.POST.get('comment'), date=datetime.date.today(),
                                             author=request.user, post=post)
            comment.save()

    if 'deletePost' in request.POST:
        post.delete()
        return redirect(request.user.profile)

    if 'deleteComment' in request.POST:
        delete_comment(request)

    if 'plusComment' in request.POST or 'minusComment' in request.POST:
        rate_comment(request)

    if 'plus' in request.POST or 'minus' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, 'You must be signed in to like!')
        elif request.user == post.author:
            messages.error(request, 'You cannot like yourself!')
        elif post.voters.filter(user=request.user).exists():
            messages.error(request, "You've already voted!")
        elif 'plus' in request.POST:                # like
            post.likes += 1
            post.voters.add(request.user.profile)
            post.save()
        else:
            post.voters.add(request.user.profile)  # dislike
            post.save()

    context['rating'] = count_rating(post)
    context['comments'] = Comment.objects.filter(post=post)
    return render(request, 'post/post_page.html', context)


def rate_comment(request):
    comment = Comment.objects.get(pk=request.POST.get('commentID'))

    if not request.user.is_authenticated:
        messages.error(request, 'You must be signed in to like!')
    elif request.user == comment.author:
        messages.error(request, 'You cannot like yourself!')
    elif comment.voters.filter(user=request.user).exists():
        messages.error(request, "You've already voted!")
    elif 'plusComment' in request.POST:  # like
        comment.likes += 1
        comment.voters.add(request.user.profile)
        comment.save()
    else:
        comment.voters.add(request.user.profile)  # dislike
        comment.save()


def delete_comment(request):
    comment = Comment.objects.filter(pk=request.POST.get('commentID'))
    comment.delete()
