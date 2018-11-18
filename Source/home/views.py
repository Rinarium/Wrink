from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, views, forms, models


def check_authentication(request):
    context = dict()
    context['authenticated'] = request.user.is_authenticated
    if context['authenticated']:
        context['user'] = request.user
    return context


def home_page(request):
    if request.method == "POST" and "delete" in request.POST:
        request.user.delete()
        logout(request)
    return render(request, 'home/home_page.html', check_authentication(request))


def sign_in_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            context = check_authentication(request)
            context['error'] = True
            return render(request, 'home/sign_in_page.html', context)
    else:
        return render(request, 'home/sign_in_page.html', check_authentication(request))


def sign_up_page(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(data=request.POST)
        if form.is_valid():
            models.User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return render(request, 'home/home_page.html', {'authenticated': True})
        else:
            context = check_authentication(request)
            context['error'] = True
            return render(request, 'home/sign_up_page.html', context)

    return render(request, 'home/sign_up_page.html', check_authentication(request))


def sign_out(request):
    logout(request)
    return redirect('home_page')


class ResetPassword(views.PasswordResetView):
    template_name = 'home/password_reset_page.html'
    success_url = 'password-reset/done'


class ResetPasswordDone(views.PasswordResetDoneView):
    template_name = 'home/password_reset_done_page.html'
