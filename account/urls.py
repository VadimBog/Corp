from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # registration and verification
    path('register/', views.register_user, name='register'),
    path('email-verification-sent/', 
        lambda request: render(request, 'account/registration/email-verification-sent.html'), 
        name='email-verification-sent'),

]