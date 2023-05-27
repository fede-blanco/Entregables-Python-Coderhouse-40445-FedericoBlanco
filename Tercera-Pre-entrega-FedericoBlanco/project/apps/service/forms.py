from django import forms

from . import models


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = "__all__"
