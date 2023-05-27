from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import forms

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "service/index.html")


def create_service(request):
    if request.method == "POST":
        form = forms.ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service:index")

    form = forms.ServiceForm()
    context = {"form": form}
    return render(request, "service/create-service.html", context)
