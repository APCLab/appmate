from rest_framework import serializers

from app.models import *

__all__ = (
    'IotSerializer',
    'KugiSerializer',
)


class IotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Iot
        fields = Iot._fields()


class KugiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kugi
        fields = Kugi._fields()
