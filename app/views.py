from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from app.forms import RegisterForm

def home(request):
    teste = {
        'x': 'teste dasdas'
    }
    return render(request,'home.html', teste)


def cadastro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = authenticate(
            username = user.username, 
            password = form.cleaned_data['password1']
            )
            login(request, user)
            print(user.foto_usuario)
            return render(request, 'home.html')
    else:
        form = RegisterForm()

    ctx = {'form': form}
    return render(request, 'cadastro.html', ctx)


def do_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            return render(request, 'home.html')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})