from django.urls import path
from . import views
from .views import home_view
from .views import form_view
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home_view, name="home_view"),
    path("form/", form_view, name='form_view'),
    path("login/", views.login_view, name="login_view"),
    path("singup/", views.singup_view, name="singup_view"),
    path("arun/", views.arun, name="arun")
]