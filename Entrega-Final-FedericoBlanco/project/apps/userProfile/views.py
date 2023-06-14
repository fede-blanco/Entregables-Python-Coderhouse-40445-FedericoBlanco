from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from . import models
from . import forms
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy


class ProfileView(DetailView):
    model = models.CustomUser
    # template_name = "index.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        # Obtén el objeto User actualmente autenticado como perfil
        return self.request.user


class ProfileUpdate(UpdateView):
    model = models.CustomUser
    form_class = forms.UserProfileForm
    template_name = "userProfile/userProfile_form.html"
    success_url = reverse_lazy("userProfile:index")

    def get_object(self, queryset=None):
        # Obtén el objeto User actualmente autenticado como perfil
        return self.request.user
