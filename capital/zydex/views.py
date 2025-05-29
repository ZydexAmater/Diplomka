from django.contrib.auth import authenticate, login as user_login, logout as user_logout

from django.http import HttpResponseRedirect
from django.shortcuts import render
from goods.models import Products, Categories
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def index(requests):
    categories = Categories.objects.all()
    products = Products.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(requests, 'zydex/index.html', context)

def about(requests):
    return render(requests, 'zydex/about.html')


def auth_view(request):
    page = request.GET.get('page', 'login')  # 'login' или 'register'

    if request.method == 'POST':
        if page == 'register':
            username = request.POST.get('username')
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')

            if password != password_confirm:
                messages.error(request, "Құпия сөздер сәйкес емес.")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Бұл логин бос емес.")
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('home')
        else:  # вход
            username = request.POST.get('login')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('zydex:index')
            else:
                messages.error(request, 'Логин немесе құпия сөз қате.')

    return render(request, 'zydex/auth.html', {'page': page})