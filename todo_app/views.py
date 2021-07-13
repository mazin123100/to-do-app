from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def todo_app(request):
    return HttpResponse('here we are')

def registerPage(request):
    context = {}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'register.html', context)