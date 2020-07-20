from django.contrib import admin
from django.urls import path,include
from account.views import SignUpView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("register",SignUpView.as_view(),name='signup'), 
    path("login",LoginView.as_view(template_name="account/login.html"),name = 'login'),
    path("",include("django.contrib.auth.urls")),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),

]
