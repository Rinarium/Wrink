from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, views


def check_authentication(request):
    context = {'authenticated': request.user.is_authenticated}
    return context


def home_page(request):
    return render(request, 'home/home_page.html', check_authentication(request))


def sign_in_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home/home_page.html', check_authentication(request))
        else:
            context = check_authentication(request)
            context['error'] = True
            return render(request, 'home/sign_in_page.html', context)
    else:
        return render(request, 'home/sign_in_page.html', check_authentication(request))


def sign_up_page(request):
    return render(request, 'home/sign_up_page.html', check_authentication(request))


def sign_out(request):
    logout(request)
    return render(request, 'home/home_page.html', check_authentication(request))


class ResetPassword(views.PasswordResetView):
    template_name = 'home/password_reset_page.html'


class ResetPasswordDone(views.PasswordResetDoneView):
    template_name = 'home/password_reset_done_page.html'
