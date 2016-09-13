from django.db import models

from rest_framework.filters import FilterSet

from app.models import Sample, SAMPLE_FIELDS

SAMPLE_FILTER_FIELDS = list(SAMPLE_FIELDS)
SAMPLE_FILTER_FIELDS.remove('img')


def fields_filter(model, fields):
    '''
    Add default filter operation.

    - ['gt', 'lt'] for ``IntegerField``
    '''
    int_type = ('AutoField', 'IntegerField')
    ret = {}

    for field in fields:
        ret[field] = ('exact',)

        if model._meta.get_field(field).get_internal_type() in int_type:
            ret[field] += ('gt', 'lt', 'gte', 'lte')

    return ret


class SampleFilter(FilterSet):
    class Meta:
        model = Sample
        fields = fields_filter(model, SAMPLE_FILTER_FIELDS)
