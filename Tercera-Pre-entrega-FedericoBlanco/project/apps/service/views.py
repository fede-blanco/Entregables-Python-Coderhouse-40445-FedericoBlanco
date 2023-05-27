from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import forms
from .models import Service

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    services = Service.objects.all()
    return render(request, "service/index.html", {"services": services})


def create_service(request):
    if request.method == "POST":
        form = forms.ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service:index")

    form = forms.ServiceForm()
    context = {"form": form}
    return render(request, "service/create-service.html", context)
