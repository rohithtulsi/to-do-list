from django.urls import path
from users.views import CustomLoginView
from users.views import RegisterPage
from users.views import ResetPasswordView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #path('register/', views.register_request, name='register'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    
]
