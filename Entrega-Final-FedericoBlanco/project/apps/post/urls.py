from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="post/index.html"), name="index"),
    path("list/", views.PostList.as_view(), name="post_list"),
    path("create/", staff_member_required(views.PostCreate.as_view()), name="post_create"),
    path("update/<int:pk>", staff_member_required(views.PostUpdate.as_view()), name="post_update"),
    path("delete/<int:pk>", staff_member_required(views.PostDelete.as_view()), name="post_delete"),
    path("detail/<int:pk>", views.PostDetail.as_view(), name="post_detail"),
]
urlpatterns += staticfiles_urlpatterns()
