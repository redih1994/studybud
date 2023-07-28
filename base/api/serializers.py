from rest_framework import serializers
from base.models import Room


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for the rooms"""

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['id']