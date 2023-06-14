from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    # Le pasamos el template name como parametro para no tener que retocar nada de la clase "LogoutView" ni tener que hacer una customizada (en views.py)
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]
urlpatterns += staticfiles_urlpatterns()
