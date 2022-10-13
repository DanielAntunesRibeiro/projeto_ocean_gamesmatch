from django.shortcuts import render, redirect

#from django.contrib.auth.models import User

def home(request):
    return render(request, 'matchapp/templates/home.html')

def login(request):
    return render(request, 'matchapp/templates/home.html')

def cadastro(request):
    return render(request, 'matchapp/templates/home.html')