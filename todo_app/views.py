from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.
def todo_app(request):
    return render(request, 'base.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user )
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('register')

    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'Username or Password is incorrect')
           
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'User succuflly logged out')
    return redirect('login')
