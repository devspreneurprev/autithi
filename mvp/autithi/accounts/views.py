from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .forms import UserLoginForm, UserRegisterForm
from proparty.models import Proparty, PropartyImage, City

# Create your views here.
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
)


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def registration_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "accounts/registration.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def home_view(request):
    context = {}
    return render(request, "accounts/home.html", context)


class HomePageView(ListView):
    model = City
    template_name = 'city_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


