from django.db import models

__all__ = (
    'Track',
    'Vehicle',
    'QueueList',
    'Evaluation',
    'Customer',
    'Driver',
)


class _UtilMixin(object):
    @classmethod
    def _fields(cls):
        return tuple(f.name for f in cls._meta.fields)


class Track(_UtilMixin, models.Model):
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    plate = models.CharField(max_length=255, blank=True, null=True)
    queue_list = models.ForeignKey('QueueList')


class Vehicle(_UtilMixin, models.Model):
    driver = models.ForeignKey('Driver')
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(auto_now=True)


class QueueList(_UtilMixin, models.Model):
    model = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(null=True)
    slongitude = models.FloatField(blank=True, null=True)
    slatitude = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    dlongitude = models.FloatField(blank=True, null=True)
    dlatitude = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    customer = models.ForeignKey('Customer')
    state = models.IntegerField(blank=True, null=True)


class Evaluation(_UtilMixin, models.Model):
    queue_list = models.ForeignKey('QueueList')
    score = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class Customer(_UtilMixin, models.Model):
    imei = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    card = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class Driver(_UtilMixin, models.Model):
    imei = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    plate = models.CharField(max_length=255, blank=True, null=True)
    car_age = models.FloatField(blank=True, null=True)
    model = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
