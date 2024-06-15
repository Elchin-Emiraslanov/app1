from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from users.forms import UserLoginForm

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'title' : 'Home - Autorisation',
        "form": form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title' : 'Home - Register',
        
    }
    return render( request, 'users/registration.html', context)

def profile(request):
    context = {
        'title' : 'Home - Cabinet'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...