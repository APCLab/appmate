from django.db import models

__all__ = (
    'Sample',
    'Demo',
)


class _UtilMixin(object):
    @classmethod
    def _fields(cls):
        return tuple(f.name for f in cls._meta.fields)

    def __str__(self):
        return 'id: {}'.format(self.id)


class Sample(_UtilMixin, models.Model):
    name = models.CharField(max_length=42)
    msg = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    img = models.ImageField(blank=True, null=True)
    checked = models.BooleanField(blank=True)
    email = models.EmailField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)


class Demo(_UtilMixin, models.Model):
    name = models.IntegerField(blank=True, null=True)
