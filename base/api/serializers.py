from rest_framework import serializers
from base.models import Room, Topic, User, Message


class RoomParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for the rooms"""

    class Meta:
        model = Room
        fields = ['id', 'name', 'updated', 'created', 'host', 'topic']
        read_only_fields = ['id']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = ['id']


class RoomDetailSerializer(RoomSerializer):
    participants = RoomParticipantSerializer(many=True, read_only=True)

    class Meta(RoomSerializer.Meta):
        model = Room
        fields = RoomSerializer.Meta.fields + ['description', 'participants']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'room', 'updated', 'created']
        read_only_fields = ['id']


class MessageDetailSerializer(MessageSerializer):
    class Meta:
        model = Message
        fields = MessageSerializer.Meta.fields + ['body']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'bio', 'avatar']
