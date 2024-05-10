from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_email_verification import send_email

User = get_user_model()

from .forms import UserCreationForm

def register_user(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_email = form.cleaned_data.get['email']
            user_username = form.cleaned_data.get['username']
            user_password = form.cleaned_data['password1']

            # create new user
            user = User.objects.create_user(
                username=user_username,
                email=user_email,
                password=user_password
            )

            user.is_active = False

            # return redirect('account:login')

    else:
        form = UserCreationForm()
    return render(request, 'account/registration/register.html', {'form': form})


