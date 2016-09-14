from rest_framework import serializers

from app.models import *

__all__ = (
    'SampleSerializer',
    'DemoSerializer',
)


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = Sample._fields()


class DemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demo
        fields = Demo._fields()
