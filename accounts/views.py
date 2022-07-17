from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def index(request):
    return redirect('home')


def register(request):
    # print(request.method)
    if request.user.is_authenticated:
        return redirect('instructions')
    else:
        form = CreateUserForm(request.POST)
        # print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("saved")
            user = form.cleaned_data.get('username')
            messages.success(request, 'Successfully signed up for ' + user)
            return redirect('login')

        contex = {'form': form}
        return render(request, 'register.html', contex)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('instructions')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')  # username from html file
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('instructions')
            else:
                messages.info(request, "Username or Password is incorrect")
                return render(request, 'login.html')
        contex = {}
        return render(request, 'login.html', contex)


def logout_user(request):
    logout(request)
    return redirect('login')
