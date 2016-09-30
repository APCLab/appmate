from django.db import models

from rest_framework.filters import FilterSet

from app.models import *

__all__ = (
    'UserFilter',
    'RestaurantFilter',
    'RateFilter',
    'MenuFilter',
    'OrderFilter',
    'ReservationFilter',
    'FavoriteFilter',
    'SensorFilter',
)


def fields_filter(model, fields):
    '''
    Add default filter operation.
    '''
    num_types = ('AutoField', 'IntegerField', 'FloatField')
    file_types = ('ImageField', 'FileField')
    ret = {}

    for field in fields:
        _type = model._meta.get_field(field).get_internal_type()

        if _type in file_types:
            continue

        ret[field] = ('exact',)

        if _type  in num_types:
            ret[field] += ('gt', 'lt', 'gte', 'lte')

    return ret


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = fields_filter(model, model._fields())


class RestaurantFilter(FilterSet):
    class Meta:
        model = Restaurant
        fields = fields_filter(model, model._fields())


class RateFilter(FilterSet):
    class Meta:
        model = Rate
        fields = fields_filter(model, model._fields())


class MenuFilter(FilterSet):
    class Meta:
        model = Menu
        fields = fields_filter(model, model._fields())


class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = fields_filter(model, model._fields())


class ReservationFilter(FilterSet):
    class Meta:
        model = Reservation
        fields = fields_filter(model, model._fields())


class FavoriteFilter(FilterSet):
    class Meta:
        model = Favorite
        fields = fields_filter(model, model._fields())


class SensorFilter(FilterSet):
    class Meta:
        model = Sensor
        fields = fields_filter(model, model._fields())
