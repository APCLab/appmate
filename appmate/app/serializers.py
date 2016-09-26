from rest_framework import serializers

from app.models import *

__all__ = (
    'UserSerializer',
    'RestaurantSerializer',
    'RateSerializer',
    'MenuSerializer',
    'OrderSerializer',
    'ReservationSerializer',
    'FavoriteSerializer',
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = User._fields()


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = Restaurant._fields()


class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = Rate._fields()


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
