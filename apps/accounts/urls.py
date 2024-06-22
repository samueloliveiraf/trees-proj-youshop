from django.urls import path

from django.contrib.auth import views as auth_views

from .views import register_user, register_account


urlpatterns = [
    path('register-user/', register_user, name='register_user'),
    path('register-account/', register_account, name='register_account'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
