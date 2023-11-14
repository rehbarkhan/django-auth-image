from .views import VideoAPIView, VideoDescriptionAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()

router.register(r'video', VideoAPIView, basename='VideoAPIView')
router.register(r'videoDescription', VideoDescriptionAPIView, basename='VideoDescription')

urlpatterns = [
    path('', include(router.urls))
]
