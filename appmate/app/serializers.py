from rest_framework import serializers

from app.models import *

__all__ = (
    'UserSerializer',
    'RestaurantSerializer',
    'RateSerializer',
    'ThumbupSerializer',
    'MenuSerializer',
    'OrderSerializer',
    'ReservationSerializer',
    'FavoriteSerializer',
    'SensorSerializer',
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = User._fields()


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    avg_point = serializers.FloatField()

    class Meta:
        model = Restaurant
        fields = Restaurant._fields() + ('avg_point',)
        read_only_fields = ('avg_point',)


class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = Rate._fields()


class ThumbupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thumbup
        fields = Thumbup._fields()


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = Menu._fields()


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = Order._fields()


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = Reservation._fields()


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorite
        fields = Favorite._fields()


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = Sensor._fields()
