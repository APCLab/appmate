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
    b_account = serializers.JSONField(read_only=True)

    class Meta:
        model = User
        fields = User._fields() + ('b_account',)


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    avg_point = serializers.FloatField(read_only=True)

    class Meta:
        model = Restaurant
        fields = Restaurant._fields() + ('avg_point',)


class RateSerializer(serializers.HyperlinkedModelSerializer):
    thumbup = serializers.IntegerField(read_only=True)

    class Meta:
        model = Rate
        fields = Rate._fields() + ('thumbup',)

    def create(self, validated_data):
        rate = super().create(validated_data)
        rest = rate.restaurant
        user = rate.user

        data = {
            'point': rate.point,
            'comment': rate.pub_comment,
            'restaurant': {
                'name': rest.name,
                'info': rest.info,
                'type': rest.type,
                'phone': rest.phone,
            }
        }
        user.store_to_block(data)

        return rate


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
