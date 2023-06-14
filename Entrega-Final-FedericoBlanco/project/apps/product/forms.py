from django import forms

from . import models


# ModelForm --> Formulario que se basa en modelos. no es tan personalizable como otras formas de formularios
# model= --> Indique da que modelo se hará# "__all__" --> Indica que nos raiga todos los fields de los elementos. Otra opcion seria nombrarlos uno por uno ["name", "price"] solo los que querramos que incluya
class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = "__all__"
        exclude = ["owner"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "stock": forms.TextInput(attrs={"class": "form-control"}),
            "owner": forms.Select(attrs={"class": "form-control"}),
        }
