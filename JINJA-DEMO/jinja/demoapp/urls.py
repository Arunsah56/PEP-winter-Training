from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jinja", views.jinja_page, name="jinja_page"),
]
