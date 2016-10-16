from django.conf import settings
from django.db import models

from bitcoin.rpc import Proxy

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

    def __str__(self):
        return 'id: {}'.format(self.id)


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
    saddress = models.TextField(blank=True, null=True)
    slongitude = models.FloatField(blank=True, null=True)
    slatitude = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    daddress = models.TextField(blank=True, null=True)
    dlongitude = models.FloatField(blank=True, null=True)
    dlatitude = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    customer = models.ForeignKey('Customer')
    driver = models.ForeignKey('Driver', null=True, blank=True)
    state = models.IntegerField(blank=True, null=True)
    arrival_time = models.DateTimeField(null=True, blank=True)


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

    @property
    def b_account(self):
        '''
        Bitcoin Account Address(es)

        This address is used for receiving payment.
        The account name is imei.
        '''
        try:
            rpc = Proxy(settings.BITCOIN_API)
            rpc.getaccountaddress(self.imei)  # create if not exists

            ret = rpc._call('getaddressesbyaccount', self.imei)
        except:
            return None
        return ret

    @property
    def b_utxo(self):
        '''
        List of bitcoin UTXOs
        '''
        try:
            rpc = Proxy(settings.BITCOIN_API)
            utxos = rpc.listunspent(addrs=self.b_account or [])
            ret = [
                {
                    'address': str(utxo['address']),
                    'amount': utxo['amount'],
                    'txid': str(utxo['outpoint']).split(':')[0],
                    'vout': str(utxo['outpoint']).split(':')[-1],
                } for utxo in utxos if utxo['spendable']
            ]
        except:
            return None
        return ret


class Driver(_UtilMixin, models.Model):
    imei = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    plate = models.CharField(max_length=255, blank=True, null=True)
    car_age = models.FloatField(blank=True, null=True)
    model = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
