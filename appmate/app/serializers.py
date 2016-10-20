from rest_framework import serializers

from app.models import *

__all__ = (
    'VoiceLogSerializer',
)


class VoiceLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VoiceLog
        fields = VoiceLog._fields()
