from django.urls import path
from . import views
urlpatterns = [
    path('auth/register', views.UserRegistrationView.as_view(), name='register'),
    path('auth/login', views.UserLoginView.as_view(), name='login'),
]
