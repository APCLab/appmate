from rest_framework import serializers

from app.models import *

__all__ = (
    'TrackSerializer',
    'VehicleSerializer',
    'QueueListSerializer',
    'EvaluationSerializer',
    'CustomerSerializer',
    'DriverSerializer',
)


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = Track._fields()


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = Vehicle._fields()


class QueueListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueueList
        fields = QueueList._fields()


class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluation
        fields = Evaluation._fields()


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = Customer._fields()


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = Driver._fields()
