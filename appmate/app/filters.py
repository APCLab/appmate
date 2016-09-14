from django.db import models

from rest_framework.filters import FilterSet

from app.models import *

__all__ = (
    'UserFilter',
    'ConcertInfoFilter',
    'ConcertBidFilter',
    'TicketFilter',
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


class ConcertInfoFilter(FilterSet):
    class Meta:
        model = ConcertInfo
        fields = fields_filter(model, model._fields())


class ConcertBidFilter(FilterSet):
    class Meta:
        model = ConcertBid
        fields = fields_filter(model, model._fields())


class TicketFilter(FilterSet):
    class Meta:
        model = Ticket
        fields = fields_filter(model, model._fields())
