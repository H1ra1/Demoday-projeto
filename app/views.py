from django.shortcuts import render

def mostrar_home(request):
    return render(request,'home.html')

def mostrar_login(request):
    return render(request,'login.html')

def mostrar_cadastro(request):
    return render(request,'cadastro.html')

def mostrar_receitas(request):
    return render(request,'receitas.html')

def mostrar_sobre(request):
    return render(request,'sobre.html')

