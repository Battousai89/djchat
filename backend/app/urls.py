from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServerViewSet, ChannelViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'servers', ServerViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
