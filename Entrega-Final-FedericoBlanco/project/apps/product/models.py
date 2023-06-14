from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# from django.utils import timezone

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField(blank=True, null=True, default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_actualization = models.DateTimeField(auto_now=True, editable=False, verbose_name="Last Actualization")
    stock = models.PositiveIntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} --  ${self.price:.2f}"

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
