from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Topic, User, Message
from .serializers import RoomSerializer, TopicSerializer, RoomParticipantSerializer, MessageSerializer, \
    MessageDetailSerializer, UserSerializer
from rest_framework import (viewsets, mixins, status)
from . import serializers


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RoomSerializer
        elif self.action == 'retrieve':
            return serializers.RoomDetailSerializer

        return self.serializer_class


class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = RoomParticipantSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MessageSerializer
        elif self.action == 'retrieve':
            return serializers.MessageDetailSerializer

        return self.serializer_class

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
