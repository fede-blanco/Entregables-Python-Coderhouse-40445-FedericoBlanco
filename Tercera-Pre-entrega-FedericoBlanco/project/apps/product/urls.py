from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-product", views.create_product, name="create-product"),
]
urlpatterns += staticfiles_urlpatterns()
