from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login(request):
    context = {
        'title' : 'Home - Autorisation'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title' : 'Home - Register'
    }
    return render( request, 'users/registration.html', context)

def profile(request):
    context = {
        'title' : 'Home - Cabinet'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...