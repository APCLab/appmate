from django.db import models

__all__ = (
    'User',
    'ConcertInfo',
    'ConcertBid',
    'Ticket',
)


class _UtilMixin(object):
    @classmethod
    def _fields(cls):
        return tuple(f.name for f in cls._meta.fields)


class User(_UtilMixin, models.Model):
    iemi = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)


class ConcertInfo(_UtilMixin, models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)


class ConcertBid(_UtilMixin, models.Model):
    user = models.ForeignKey('User')
    rank = models.CharField(max_length=255, blank=True, null=True)
    a_price = models.FloatField(blank=True, null=True)
    b_price = models.FloatField(blank=True, null=True)
    c_price = models.FloatField(blank=True, null=True)
    d_price = models.FloatField(blank=True, null=True)
    e_price = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class Ticket(_UtilMixin, models.Model):
    concert_info = models.ForeignKey('ConcertInfo')
    region = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, auto_now=True)
    user = models.ForeignKey('User', null=True, blank=True)
