from django.urls import path
from users.views import CustomLoginView
from users.views import RegisterPage
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #path('register/', views.register_request, name='register'),
    path('register/', RegisterPage.as_view(), name='register'),
]
