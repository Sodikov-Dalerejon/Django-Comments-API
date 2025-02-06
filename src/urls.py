from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserTextViewSet
router = DefaultRouter()
router.register(r'users', UserTextViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
