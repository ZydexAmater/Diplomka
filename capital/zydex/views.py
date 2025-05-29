from django.contrib.auth import authenticate, login as user_login, logout as user_logout

from django.contrib.auth.decorators import login_required


from .forms import NurseVisitForm

from .models import NurseVisit

from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.


from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import NurseVisitForm


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def index(requests):
    return render(requests, 'zydex/index.html')

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
                return redirect('zydex:nurse_visit')
            else:
                messages.error(request, 'Логин немесе құпия сөз қате.')

    return render(request, 'zydex/auth.html', {'page': page})



def nurse_visit_view(request):
    if request.method == 'POST':
        form = NurseVisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zydex:visit_success')  # создадим позже
    else:
        form = NurseVisitForm()
    return render(request, 'zydex/visit_form.html', {'form': form})

def visit_success(request):
    return render(request, 'zydex/success.html')


def nurse_visit_list(request):
    visits = NurseVisit.objects.order_by('-timestamp')  # последние сверху
    return render(request, 'zydex/visit_list.html', {'visits': visits})


def edit_visit(request, pk):
    visit = get_object_or_404(NurseVisit, pk=pk)
    if request.method == 'POST':
        form = NurseVisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Жазба сәтті өзгертілді.')
            return redirect('zydex:nurse_visit_list')
    else:
        form = NurseVisitForm(instance=visit)
    return render(request, 'zydex/edit_visit.html', {'form': form})

def delete_visit(request, pk):
    visit = get_object_or_404(NurseVisit, pk=pk)
    if request.method == 'POST':
        visit.delete()
        messages.success(request, 'Жазба жойылды.')
        return redirect('zydex:nurse_visit_list')
    return render(request, 'zydex/delete_confirm.html', {'visit': visit})


@login_required
def nurse_visit_list(request):
    query = request.GET.get('q')
    if query:
        visits = NurseVisit.objects.filter(name__icontains=query)
    else:
        visits = NurseVisit.objects.all().order_by('-timestamp')

    return render(request, 'zydex/visit_list.html', {'visits': visits})

@login_required
def edit_visit(request, pk):
    visit = get_object_or_404(NurseVisit, pk=pk)
    if request.method == 'POST':
        form = NurseVisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Жазба сәтті өзгертілді.')
            return redirect('zydex:nurse_visit_list')
    else:
        form = NurseVisitForm(instance=visit)
    return render(request, 'zydex/edit_visit.html', {'form': form})

@login_required
def delete_visit(request, pk):
    visit = get_object_or_404(NurseVisit, pk=pk)
    if request.method == 'POST':
        visit.delete()
        messages.success(request, 'Жазба жойылды.')
        return redirect('zydex:nurse_visit_list')
    return render(request, 'zydex/delete_confirm.html', {'visit': visit})

