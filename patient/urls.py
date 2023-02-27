from django.contrib import admin
from django.urls import path, include
from .views import signUp, logIn, Home, logOut, Test
urlpatterns = [

    path('', signUp, name='signup-page'),
    path('home/', Home, name='home'),
    path('signup/', signUp, name='signup-page'),
    path('login/', logIn, name='login-page'),
    path('logout/', logOut, name='logout-page'),
    path('test/', Test, name='test')

]
