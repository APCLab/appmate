from django.db import models

from django_filters.rest_framework import FilterSet

from app.models import *

__all__ = (
    'IotFilter',
    'KugiFilter',
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


class IotFilter(FilterSet):
    class Meta:
        model = Iot
        fields = fields_filter(model, model._fields())


class KugiFilter(FilterSet):
    class Meta:
        model = Kugi
        fields = fields_filter(model, model._fields())
