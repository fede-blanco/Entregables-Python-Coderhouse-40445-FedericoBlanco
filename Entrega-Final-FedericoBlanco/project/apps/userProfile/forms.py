from django import forms

from . import models


# ModelForm --> Formulario que se basa en modelos. no es tan personalizable como otras formas de formularios
# model= --> Indique da que modelo se hará# "__all__" --> Indica que nos raiga todos los fields de los elementos. Otra opcion seria nombrarlos uno por uno ["name", "price"] solo los que querramos que incluya
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        # fields = "__all__"
        fields = [
            # "username",
            "first_name",
            "last_name",
            "email",
            # "password",
            "description",
            "image",
            "website",
        ]
        # exclude = ["date"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "website": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateTimeInput(attrs={"class": "form-control"}),
            "last_actualization": forms.DateTimeInput(attrs={"class": "form-control"}),
        }
