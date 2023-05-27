from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-service", views.create_service, name="create-service"),
]
urlpatterns += staticfiles_urlpatterns()
