from django.db import models

__all__ = (
    'Sample',
    'Demo',
)


class _UtilMixin(object):
    @classmethod
    def _fields(cls):
        return tuple(f.name for f in cls._meta.fields)


class Sample(_UtilMixin, models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    img = models.ImageField(blank=True, null=True)
    checked = models.BooleanField(blank=True)
    email = models.EmailField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)


class Demo(_UtilMixin, models.Model):
    name = models.IntegerField(blank=True, null=True)
