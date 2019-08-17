from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

from django.views.generic.list import ListView

from .models import City
from proparty.models import Proparty, PropartyImage

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


class PropertyListView(ListView):
    model = Proparty
    template_name = 'property_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Proparty.objects.filter(address__city='sylhet')
        obj2 = Proparty.objects.filter(address__city='dhanmondi')
        context['obj'] = obj
        context['obj2'] = obj2
        print(obj)
        return context


# class PropertyListView(ListView):
#     model = Proparty
#     template_name = 'property_list.html'


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         city_list = Address.objects.order_by().values_list('city').distinct()
#         city_list = [each_city[0] for each_city in city_list]
#         context["city_list"] = city_list
#         for each_city in city_list:
#             if each_city:
#                 obj = Proparty.objects.filter(address__city=each_city)
#         return context
