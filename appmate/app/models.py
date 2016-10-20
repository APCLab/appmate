from django.db import models

__all__ = (
    'VoiceLog',
)


class _UtilMixin(object):
    @classmethod
    def _fields(cls):
        return tuple(f.name for f in cls._meta.fields)

    def __str__(self):
        return 'id: {}'.format(self.id)


class VoiceLog(_UtilMixin, models.Model):
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    sentence = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
