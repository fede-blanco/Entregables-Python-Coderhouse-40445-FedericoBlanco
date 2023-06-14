from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import forms, models
from .models import Product
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


# def index(request: HttpRequest) -> HttpResponse:
#     products = Product.objects.all()
#     # datos = {"productos": products}
#     return render(request, "product/index.html", {"products": products})


# def product_list(request: HttpRequest) -> HttpResponse:
#     products = Product.objects.all()
#     # datos = {"productos": products}
#     return render(request, "product/product-list.html", {"products": products})


class ProductList(ListView):
    model = models.Product

    def get_queryset(self):
        """Devuelve los productos de la categoria escrita por el usuario en el formulario de búsqueda"""
        # Si la búsqueda tiene algún texto introducido, devuelve todos los productos que contengan dicho texto y los introdce en object_list
        if self.request.GET.get("consulta"):
            # En query se guarda el contenido  que haya en la variable "consulta" de la request
            query = self.request.GET.get("consulta")
            object_list = models.Product.objects.filter(name__icontains=query)
        else:
            # Si no, devuelve todos los productos y los introduce en object_list
            object_list = models.Product.objects.all()
            # retorna object_list que es la lista de productos
        return object_list


class ProductCreate(LoginRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy("product:product_list")

    # Esta funcion hara que se agregue como owner del elemento creado el usuario que este autenticado en el momento
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy("product:product_list")


class ProductDelete(DeleteView):
    model = models.Product
    success_url = reverse_lazy("product:product_list")


class ProductDetail(DetailView):
    model = models.Product


# def create_product(request):
#     if request.method == "POST":
#         form = forms.ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("product:index")

#     form = forms.ProductForm()
#     context = {"form": form}
#     return render(request, "product/create-product.html", context)
