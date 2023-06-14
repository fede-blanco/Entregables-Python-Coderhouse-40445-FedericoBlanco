from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="service/index.html"), name="index"),
    path("list/", views.ServiceList.as_view(), name="service_list"),
    path("create/", staff_member_required(views.ServiceCreate.as_view()), name="service_create"),
    path("update/<int:pk>", staff_member_required(views.ServiceUpdate.as_view()), name="service_update"),
    path("delete/<int:pk>", staff_member_required(views.ServiceDelete.as_view()), name="service_delete"),
    path("detail/<int:pk>", views.ServiceDetail.as_view(), name="service_detail"),
]
urlpatterns += staticfiles_urlpatterns()
