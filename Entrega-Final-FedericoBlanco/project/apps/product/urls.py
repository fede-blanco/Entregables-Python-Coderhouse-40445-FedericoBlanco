from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", TemplateView.as_view(template_name="product/index.html"), name="index"),
    path("list/", views.ProductList.as_view(), name="product_list"),
    path("create/", staff_member_required(views.ProductCreate.as_view()), name="product_create"),
    path("update/<int:pk>", staff_member_required(views.ProductUpdate.as_view()), name="product_update"),
    path("delete/<int:pk>", staff_member_required(views.ProductDelete.as_view()), name="product_delete"),
    path("detail/<int:pk>", views.ProductDetail.as_view(), name="product_detail"),
]
urlpatterns += staticfiles_urlpatterns()
