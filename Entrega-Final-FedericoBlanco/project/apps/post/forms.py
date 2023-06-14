from django import forms

from . import models


# ModelForm --> Formulario que se basa en modelos. no es tan personalizable como otras formas de formularios
# model= --> Indique da que modelo se hará# "__all__" --> Indica que nos raiga todos los fields de los elementos. Otra opcion seria nombrarlos uno por uno ["name", "price"] solo los que querramos que incluya
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
        exclude = ["author"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "subtitle": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
        }
