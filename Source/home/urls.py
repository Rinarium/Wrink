from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path(r'^$', views.home_page, name='home_page'),
    re_path(r'^sign-in$', views.sign_in_page, name='sign_in_page'),
    re_path(r'^sign-in/password-reset$', views.ResetPassword.as_view(), name='password_reset_page'),
    re_path(r'^sign-in/password-reset/done$', views.ResetPasswordDone.as_view(), name='password_reset_done_page'),
    re_path(r'^sign-up$', views.sign_up_page, name='sign_up_page'),
    re_path(r'^sign-out$', views.sign_out, name='sign_out'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
