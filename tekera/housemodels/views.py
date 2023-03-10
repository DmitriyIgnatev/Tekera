from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

from .forms import LoginForm, SignUpForm
from .models import MyModel


def home(request):
    return render(request, 'mainscreen.html')


class Login(LoginView):
    form_class = LoginForm
    success_url = reverse_lazy('housemodels:housemodels')

    def get_success_url(self):
        return self.success_url


def signup(request):
    form = SignUpForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('housemodels:housemodels')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('housemodels:housemodels')


def main(request):
    models = MyModel.objects.all()
    context = {
        'houses': models
    }

    return render(request, 'main.html', context)


def detail(request, pk):
    models = MyModel.objects.get(pk=pk)
    context = {
        'house': models
    }
    return render(request, 'detail.html', context)
