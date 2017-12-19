from django.shortcuts import render
from first_app.forms import UserForm
from first_app.models import UserProfileInfo

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    return render(request, 'first_app/login_page.html')

def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'first_app/reg_page.html',{'user_form':user_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile_view'))
            else:
                return HttpResponse('Your account is not active')
        else:
            print('Some one tried to login and failed')

    else:
        return(render, 'first_app/login_page.html')

@login_required
def user_logout():
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))

@login_required
def profile_view(request, username):
    profile = request.username
    return render(request, 'first_app/profile.html',args = profile)
