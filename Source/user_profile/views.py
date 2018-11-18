from django.shortcuts import render, redirect
from django.contrib import messages
from home.views import check_authentication as authenticated
from .forms import UserForm, ProfileForm
from .models import Profile
from post.models import Post
from django.core.exceptions import ObjectDoesNotExist


def count_rating(user):
    try:
        rating = user.profile.likes / user.profile.voters.count()
    except ZeroDivisionError:
        rating = 1.0
    return rating


def profile_page(request, profile_id):
    context = authenticated(request)
    if request.method == 'POST' and 'save' in request.POST:
        user_profile = request.user
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        try:
            profile = Profile.objects.get(pk=profile_id)
            user_profile = profile.user
            context['posts'] = Post.objects.filter(author=user_profile)
        except ObjectDoesNotExist:
            return redirect('home_page')

        if request.method == 'POST':
            if not request.user.is_authenticated:
                messages.error(request, 'You must be signed in to like!')
            elif request.user == user_profile:
                messages.error(request, 'You cannot like yourself!')
            elif user_profile.profile.voters.filter(user=request.user).exists():
                messages.error(request, "You've already voted!")
            elif 'plus' in request.POST:                                        # like
                user_profile.profile.likes += 1
                user_profile.profile.voters.add(request.user.profile)
                user_profile.save()
            else:
                user_profile.profile.voters.add(request.user.profile)           # dislike
                user_profile.save()

    context['user_profile'] = user_profile
    context['rating'] = count_rating(user_profile)
    return render(request, 'profile/profile_page.html', context)
