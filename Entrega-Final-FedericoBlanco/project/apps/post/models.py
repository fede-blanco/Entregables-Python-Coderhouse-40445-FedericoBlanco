from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_actualization = models.DateTimeField(auto_now=True, editable=False, verbose_name="Last Actualization")
    image = models.ImageField(upload_to="posts", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} -- {self.author} -- {self.last_actualization}"

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
