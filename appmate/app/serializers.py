from rest_framework import serializers

from app.models import *

__all__ = (
    'UserSerializer',
    'ConcertInfoSerializer',
    'ConcertBidSerializer',
    'TicketSerializer',
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    b_account = serializers.JSONField(read_only=True)

    class Meta:
        model = User
        fields = User._fields() + ('b_account',)


class ConcertInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConcertInfo
        fields = ConcertInfo._fields()


class ConcertBidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConcertBid
        fields = ConcertBid._fields()


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = Ticket._fields()
