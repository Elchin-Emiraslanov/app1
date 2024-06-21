from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from traitlets import Instance
from users.forms import ProfileForm, UserLoginForm, UserCreationForm, UserRegistrartion



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
                messages.success(request, f"{username}, Siz hesaba daxil oldunuz")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))

                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'title' : 'Home - Autorisation',
        "form": form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrartion(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Siz uğurla qeydiyyatdan keçdiz və daxil olduz")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrartion()

    context = {
        'title' : 'Home - Register',
        "form": form
        
    }
    return render( request, 'users/registration.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Səhifə uğurla yeniləndi!")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title' : 'Home - Cabinet',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Səhifədən çıxış edildi.")
    auth.logout(request)
    return redirect(reverse('main:index'))

