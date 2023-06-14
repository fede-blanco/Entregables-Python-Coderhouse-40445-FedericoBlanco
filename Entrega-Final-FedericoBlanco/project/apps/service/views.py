from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import forms, models
from .models import Service
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


# def index(request: HttpRequest) -> HttpResponse:
#     services = Service.objects.all()
#     return render(request, "service/index.html", {"services": services})


class ServiceList(ListView):
    model = models.Service

    def get_queryset(self):
        """Devuelve los productos de la categoria escrita por el usuario en el formulario de búsqueda"""
        # Si la búsqueda tiene algún texto introducido, devuelve todos los productos que contengan dicho texto y los introdce en object_list
        if self.request.GET.get("consulta"):
            # En query se guarda el contenido  que haya en la variable "consulta" de la request
            query = self.request.GET.get("consulta")
            object_list = models.Service.objects.filter(name__icontains=query)
        else:
            # Si no, devuelve todos los productos y los introduce en object_list
            object_list = models.Service.objects.all()
            # retorna object_list que es la lista de productos
        return object_list


class ServiceCreate(LoginRequiredMixin, CreateView):
    model = models.Service
    form_class = forms.ServiceForm
    success_url = reverse_lazy("service:service_list")

    # Esta funcion hara que se agregue como owner del elemento creado el usuario que este autenticado en el momento
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ServiceUpdate(UpdateView):
    model = models.Service
    form_class = forms.ServiceForm
    success_url = reverse_lazy("service:service_list")


class ServiceDelete(DeleteView):
    model = models.Service
    success_url = reverse_lazy("service:service_list")


class ServiceDetail(DetailView):
    model = models.Service


# def create_service(request):
#     if request.method == "POST":
#         form = forms.ServiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("service:index")

#     form = forms.ServiceForm()
#     context = {"form": form}
#     return render(request, "service/create-service.html", context)
