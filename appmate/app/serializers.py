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
    b_account = serializers.JSONField(read_only=True)

    class Meta:
        model = Ticket
        fields = Ticket._fields() + ('b_account',)

    def create(self, validated_data):
        ticket = super().create(validated_data)

        concert = ticket.concert_info
        sender = ticket.prev.user if ticket.prev else User.objects.get(
            iemi='master')
        data = {
            'concert': {
                'name': concert.name,
                'date': str(concert.date.astimezone(tz=None)),
                'location': concert.location,
            },
            'token': ticket.token,
            'region': ticket.region,
            'price': ticket.price,
        }
        sender.store_to_block(data, ticket.user)
        return ticket
