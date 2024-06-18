from atexit import register
from django.urls import path 

from users import *
from users.views import login, logout, profile, registration, users_cart

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        login,
        name='login',
    ),

    path(
        'registration/',
        registration,
        name='registration',
    ),

    path(
        'profile/',
        profile,
        name='profile',
    ),

    path(
        'users-cart/',
        users_cart,
        name='users-cart',
    ),

    path(
        'logout/',
        logout,
        name='logout',
        ),

]
