from django.shortcuts import render

def home(request):
    return render(request, 'gamesmatch/matchapp/templates/home.html')
