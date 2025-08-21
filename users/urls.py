"""Defines URL patterns for users"""

from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
]