from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import forms

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "product/index.html")


def create_product(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product:index")

    form = forms.ProductForm()
    context = {"form": form}
    return render(request, "product/create-product.html", context)
