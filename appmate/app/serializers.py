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

    def create(self, validated_data):
        evaluation = super().create(validated_data)

        ql = evaluation.queue_list
        customer = evaluation.queue_list.customer

        data = {
            'score': evaluation.score,
            'saddress': ql.saddress,
            'slongitude': ql.slongitude,
            'slatitude': ql.slatitude,
            'price': ql.price,
            'daddress': ql.daddress,
            'dlongitude': ql.dlongitude,
            'dlatitude': ql.dlatitude,
            'driver': ql.driver.imei
        }
        customer.store_to_block(data)

        return evaluation


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    b_account = serializers.JSONField(read_only=True)
    b_utxo = serializers.JSONField(read_only=True)
    b_balance = serializers.FloatField(read_only=True)

    class Meta:
        model = Customer
        fields = Customer._fields() + (
            'b_account', 'b_utxo', 'b_balance')


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = Driver._fields()
