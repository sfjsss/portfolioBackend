from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProjectViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]