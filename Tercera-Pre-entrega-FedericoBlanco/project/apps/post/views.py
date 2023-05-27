from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import forms

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "post/index.html")


def create_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post:index")

    form = forms.PostForm()
    context = {"form": form}
    return render(request, "post/create-post.html", context)
