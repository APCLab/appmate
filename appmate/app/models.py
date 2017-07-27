from django.db import models

__all__ = (
    'Iot',
    'Kugi',
)


class _UtilMixin(object):
    @classmethod
    def _fields(cls):
        return tuple(f.name for f in cls._meta.fields)

    def __str__(self):
        return 'id: {}'.format(self.id)


class Iot(_UtilMixin, models.Model):
    hostname = models.CharField(max_length=255)
    humi = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    light = models.IntegerField(blank=True, null=True)
    touch = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now=True)
    cell1 = models.TextField(blank=True, null=True)
    cell2 = models.TextField(blank=True, null=True)
    cell3 = models.TextField(blank=True, null=True)
    cell4 = models.TextField(blank=True, null=True)
    cell5 = models.TextField(blank=True, null=True)


class Kugi(_UtilMixin, models.Model):
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    cell1 = models.TextField(blank=True, null=True)
    cell2 = models.TextField(blank=True, null=True)
    cell3 = models.TextField(blank=True, null=True)
    cell4 = models.TextField(blank=True, null=True)
    cell5 = models.TextField(blank=True, null=True)
    cell6 = models.TextField(blank=True, null=True)
    cell7 = models.TextField(blank=True, null=True)
