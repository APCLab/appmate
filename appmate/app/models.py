import json
import logging

from binascii import hexlify

from django.conf import settings
from django.db import models

from bitcoin.core import COIN
from bitcoin.rpc import Proxy

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

    def __str__(self):
        return 'id: {}'.format(self.id)


class User(_UtilMixin, models.Model):
    iemi = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)

    @property
    def b_account(self):
        '''
        Bitcoin Account Address(es)

        This address is used for receiving payment.
        The account name is imei.
        '''
        id_ = self.iemi
        try:
            rpc = Proxy(settings.BITCOIN_API)
            if id_ not in rpc._call('listaccounts'):
                rpc.getaccountaddress(id_)  # create if not exists
                ret = rpc._call('getaddressesbyaccount', id_)
                rpc._call('generatetoaddress', 10, ret[0])

            ret = rpc._call('getaddressesbyaccount', id_)
        except Exception as err:
            logging.error(err)
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

    def create_tx(self, data, send_to):
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
        while txin_amount <= 0.53:
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
            out_addr: round(txin_amount - 0.52, 6),
            send_to: round(0.5, 6),
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

    def store_to_block(self, data, send_to):
        '''
        Create and send the transaction

        :type data: str or dict
        :type send_to: User object
        :return: the tx id
        '''
        tx = self.create_tx(data, send_to.b_account[0])
        if not tx:
            return False

        try:
            rpc = Proxy(settings.BITCOIN_API)
            txid = rpc._call('sendrawtransaction', tx)
        except Exception as err:
            logging.error(err)
            return False
        return txid


class ConcertInfo(_UtilMixin, models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)


class ConcertBid(_UtilMixin, models.Model):
    user = models.ForeignKey('User')
    concert_info = models.ForeignKey('ConcertInfo')
    a_rank = models.CharField(max_length=255, blank=True, null=True)
    b_rank = models.CharField(max_length=255, blank=True, null=True)
    c_rank = models.CharField(max_length=255, blank=True, null=True)
    d_rank = models.CharField(max_length=255, blank=True, null=True)
    e_rank = models.CharField(max_length=255, blank=True, null=True)
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
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user = models.ForeignKey('User')
    prev = models.ForeignKey('Ticket', null=True, blank=True)
