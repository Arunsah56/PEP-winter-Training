
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add-task'),
    path('update/<int:pk>/', views.update_task, name='update-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle-task'),
]
