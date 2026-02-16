from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from .views import CreateStudent

router = DefaultRouter()
router.register(r'Students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path("create-student/", CreateStudent.as_view()),
]