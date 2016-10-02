from django.db import models

__all__ = (
    'User',
    'Restaurant',
    'Rate',
    'Thumbup',
    'Menu',
    'Order',
    'Reservation',
    'Favorite',
    'Sensor',
)


class _UtilMixin(object):
    @classmethod
    def _fields(cls):
        return tuple(f.name for f in cls._meta.fields)


class User(_UtilMixin, models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)


class Restaurant(_UtilMixin, models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    total_seat = models.IntegerField(blank=True, null=True)
    empty_seat = models.IntegerField(blank=True, null=True)
    longtitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)

    @property
    def avg_point(self):
        qs = self.rate_set.all()
        n = len(qs)
        if not n :
            return 0
        return sum(rate.point for rate in qs) / n


class Rate(_UtilMixin, models.Model):
    restaurant = models.ForeignKey('Restaurant')
    user = models.ForeignKey('User')
    point = models.IntegerField(blank=True, null=True)
    pub_comment = models.TextField(blank=True, null=True)
    priv_comment = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class Thumbup(_UtilMixin, models.Model):
    user = models.ForeignKey('User')
    rate = models.ForeignKey('Rate')
    check = models.BooleanField(blank=True)


class Menu(_UtilMixin, models.Model):
    restaurant = models.ForeignKey('Restaurant')
    name = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)


class Order(_UtilMixin, models.Model):
    restaurant = models.ForeignKey('Restaurant')
    user = models.ForeignKey('User')
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    seat_number = models.CharField(max_length=255, blank=True, null=True)
    menu = models.ForeignKey('Menu')
    count = models.IntegerField(blank=True, null=True)


class Reservation(_UtilMixin, models.Model):
    user = models.ForeignKey('User')
    seat_number = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(auto_now=True)
    res_time = models.DateTimeField()
    available = models.BooleanField(blank=True)


class Favorite(_UtilMixin, models.Model):
    user = models.ForeignKey('User')
    restaurant = models.ForeignKey('Restaurant')


class Sensor(_UtilMixin, models.Model):
    check = models.IntegerField(blank=True, null=True)
