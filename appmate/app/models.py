import json
import logging

from binascii import hexlify

from django.conf import settings
from django.db import models

from bitcoin.core import COIN
from bitcoin.rpc import Proxy

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

    def __str__(self):
        return 'id: {}'.format(self.id)


class User(_UtilMixin, models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)

    @property
    def b_account(self):
        '''
        Bitcoin Account Address(es)

        This address is used for receiving payment.
        The account name is imei.
        '''
        id_ = str(self.id)
        try:
            rpc = Proxy(settings.BITCOIN_API)
            if id_ not in rpc._call('listaccounts'):
                rpc.getaccountaddress(id_)  # create if not exists
                ret = rpc._call('getaddressesbyaccount', id_)
                rpc._call('generatetoaddress', 10, ret[0])

            ret = rpc._call('getaddressesbyaccount', id_)
        except Exception as err:
            print(err)
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
                    'amount': utxo['amount'] / COIN,
                    'txid': str(utxo['outpoint']).split(':')[0],
                    'vout': int(str(utxo['outpoint']).split(':')[-1]),
                } for utxo in utxos if utxo['spendable']
            ]
        except:
            return None
        return ret

    def create_tx(self, data=None):
        '''
        Create a transaction with ``data`` as payload.

        We always send 0.2 COIN.

        :type data: str or dict

        :return: False if creating failed.
                 The hex of tx if created.
        '''
        # txin
        txin = []
        txin_amount = 0.0
        out_addr = None
        utxoes = self.b_utxo
        while txin_amount <= 0.03:
            if not utxoes:
                return False

            u = utxoes.pop()
            txin.append({'txid': u['txid'],
                         'vout': u['vout']})
            txin_amount += u['amount']

            if not out_addr:
                out_addr = u['address']

        # txout
        txout = {
            out_addr: round(txin_amount- 0.02, 6),
        }
        if data:
            if isinstance(data, (dict, list, tuple)):
                data = json.dumps(data)
            txout['data'] = hexlify(data.encode()).decode()

        try:
            rpc = Proxy(settings.BITCOIN_API)
            raw_tx = rpc._call('createrawtransaction', txin, txout)
            ret = rpc._call('signrawtransaction', raw_tx)['hex']
        except Exception as err:
            logging.error(err)
            logging.error('txin_amount = %s', txin_amount)
            logging.error('txin %s', txin)
            logging.error('txout %s', txout)
            return False
        return ret

    def store_to_block(self, data):
        '''
        Create and send the transaction

        :type data: str or dict
        :return: the tx id
        '''
        tx = self.create_tx(data)
        if not tx:
            return False

        try:
            rpc = Proxy(settings.BITCOIN_API)
            txid = rpc._call('sendrawtransaction', tx)
        except Exception as err:
            logging.error(err)
            return False
        return txid


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

    @property
    def thumbup(self):
        return self.thumbup_set.filter(check=True).count()


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
    check = models.IntegerField(blank=True, default=0)


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
