from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-post/", views.create_post, name="create-post"),
]
urlpatterns += staticfiles_urlpatterns()
