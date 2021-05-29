from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm
from Shop import models as shop_modals


def sign_up(request):
    form = UserCreateForm()
    context = {'form': form}
    if request.method == 'POST':
        form_data = UserCreateForm(request.POST)
        if form_data.is_valid():
            sign_up = form_data.save(commit=False)
            sign_up.password = make_password(form_data.cleaned_data['password'])
            sign_up.save()
            user_auth = authenticate(email=form_data['email'].data, password=form_data['password'].data)
            if user_auth:
                return redirect('User:dashboard')
        else:
            context.update({'form': form, 'errors': form_data.errors})
    return render(request, 'User/signup.html', context)


def login(request):
    form = UserLoginForm()
    context = {'form': form}
    if request.method == 'POST':
        form_data = UserLoginForm(request.POST)
        user_auth = authenticate(email=form_data['email'].data, password=form_data['password'].data)
        if user_auth:
            return redirect('User:dashboard')
    return render(request, 'User/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('User:login')


def dashboard(request):
    return render(request, 'User/dashboard.html', {'products': shop_modals.Product.objects.all()})
