from django.db import models

from django_filters.rest_framework import FilterSet

from app.models import *

__all__ = (
    'SampleFilter',
    'DemoFilter',
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


class SampleFilter(FilterSet):
    class Meta:
        model = Sample
        fields = fields_filter(model, model._fields())


class DemoFilter(FilterSet):
    class Meta:
        model = Demo
        fields = fields_filter(model, model._fields())
