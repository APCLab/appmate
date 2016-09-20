from django.db import models

from rest_framework.filters import FilterSet

from app.models import *

__all__ = (
    'TrackFilter',
    'VehicleFilter',
    'QueueListFilter',
    'EvaluationFilter',
    'CustomerFilter',
    'DriverFilter',
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


class TrackFilter(FilterSet):
    class Meta:
        model = Track
        fields = fields_filter(model, model._fields())


class VehicleFilter(FilterSet):
    class Meta:
        model = Vehicle
        fields = fields_filter(model, model._fields())


class QueueListFilter(FilterSet):
    class Meta:
        model = QueueList
        fields = fields_filter(model, model._fields())


class EvaluationFilter(FilterSet):
    class Meta:
        model = Evaluation
        fields = fields_filter(model, model._fields())


class CustomerFilter(FilterSet):
    class Meta:
        model = Customer
        fields = fields_filter(model, model._fields())


class DriverFilter(FilterSet):
    class Meta:
        model = Driver
        fields = fields_filter(model, model._fields())
