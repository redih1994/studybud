from django.urls import path, include
from .views import TopicViewSet, RoomViewSet, ParticipantViewSet, MessageViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'message', MessageViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

]