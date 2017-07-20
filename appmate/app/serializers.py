from rest_framework import serializers

from app.models import *

__all__ = (
    'IotSerializer',
)


class IotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Iot
        fields = Iot._fields()
