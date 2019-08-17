from django.shortcuts import render
from app.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

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


def login(request):
    return render(request, 'login.html')


