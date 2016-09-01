from django.db import models


class Sample(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, auto_now=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now=True)
    img = models.ImageField(blank=True, null=True)
    checked = models.BooleanField(blank=True)
    email = models.EmailField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Sample id: {}'.format(self.id)


SAMPLE_FIELDS = (
    'id',
    'name',
    'msg',
    'date',
    'timestamp',
    'img',
    'checked',
    'email',
    'index')
