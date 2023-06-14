from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.ProfileView.as_view(template_name="userProfile/index.html"), name="index"),
    path("update/<int:pk>/", views.ProfileUpdate.as_view(), name="userProfile_update"),
]
urlpatterns += staticfiles_urlpatterns()
