from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import forms, models
from .models import Post
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


# def index(request: HttpRequest) -> HttpResponse:
#     posts = Post.objects.all()
#     return render(request, "post/index.html", {"posts": posts})


class PostList(ListView):
    model = models.Post

    def get_queryset(self):
        """Devuelve los productos de la categoria escrita por el usuario en el formulario de búsqueda"""
        # Si la búsqueda tiene algún texto introducido, devuelve todos los productos que contengan dicho texto y los introdce en object_list
        if self.request.GET.get("consulta"):
            # En query se guarda el contenido  que haya en la variable "consulta" de la request
            query = self.request.GET.get("consulta")
            object_list = models.Post.objects.filter(title__icontains=query)
        else:
            # Si no, devuelve todos los productos y los introduce en object_list
            object_list = models.Post.objects.all()
            # retorna object_list que es la lista de productos
        return object_list


class PostCreate(LoginRequiredMixin, CreateView):
    model = models.Post
    form_class = forms.PostForm
    success_url = reverse_lazy("post:post_list")

    # Esta funcion hara que se agregue como owner del elemento creado el usuario que este autenticado en el momento
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    success_url = reverse_lazy("post:post_list")


class PostDelete(DeleteView):
    model = models.Post
    success_url = reverse_lazy("post:post_list")


class PostDetail(DetailView):
    model = models.Post


# def create_post(request):
#     if request.method == "POST":
#         form = forms.PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("post:index")

#     form = forms.PostForm()
#     context = {"form": form}
#     return render(request, "post/create-post.html", context)
