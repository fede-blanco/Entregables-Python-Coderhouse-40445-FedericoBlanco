from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import forms
from .models import Product

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    # datos = {"productos": products}
    return render(request, "product/index.html", {"products": products})


def create_product(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product:index")

    form = forms.ProductForm()
    context = {"form": form}
    return render(request, "product/create-product.html", context)
