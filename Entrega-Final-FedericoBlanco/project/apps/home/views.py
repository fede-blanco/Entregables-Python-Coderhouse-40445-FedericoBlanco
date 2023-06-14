from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from . import forms


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "home/about.html")


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        # Al usar funciones hay que pasarle los datos, y nosotros al darle click a "iniciar sesion" se guardan en la varaible "POST" de request
        form = forms.CustomAuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            # Los nombres internos de django son "username" y "password" (son los que uso como id del input en el form)
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # Los nombres internos de django son "username" y "password"
            user = authenticate(username=user, password=password)
            if user is not None:  # --> Osea que tiene algo dentro
                login(request, user)
                return render(request, "home/index.html", {"mensaje": f"Bienvenido {user}!"})
    else:  # --> Si entra por primera vez a este controlador
        form = forms.CustomAuthenticationForm()
    # le pasamos el form por contexto que es el que utilizara en el HTML
    return render(request, "home/login.html", {"form": form})


# Registro basado en funciones
def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": "Usuario creado 👌"})
    else:
        # form = UserCreationForm()
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})
