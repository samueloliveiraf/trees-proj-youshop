from django.urls import path

from django.contrib.auth import views as auth_views

from .views import register_user, register_account, users_list, toggle_user_status


urlpatterns = [
    path('register-user/', register_user, name='register_user'),
    path('register-account/', register_account, name='register_account'),

    path('users/', users_list, name='users_list'),
    path('toggle_user_status/<str:user_id>/', toggle_user_status, name='toggle_user_status'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
