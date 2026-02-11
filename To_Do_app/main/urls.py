
from django.urls import path
from .views import HomeView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', TaskCreateView.as_view(), name='add-task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
]
