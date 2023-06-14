from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True, null=True, default="")
    website = models.CharField(max_length=100, blank=True, null=True, default="")
    image = models.ImageField(upload_to="avatars", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_actualization = models.DateTimeField(auto_now=True, editable=False, verbose_name="Last Actualization")

    def __str__(self) -> str:
        return f"{self.username} -- {self.email} -- {self.last_actualization}"

    class Meta:
        verbose_name = "custom User"
        verbose_name_plural = "custom Users"
