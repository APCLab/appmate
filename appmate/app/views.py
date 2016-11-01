from random import randint
from uuid import uuid4

from django.shortcuts import render

from rest_framework import filters, viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'UserViewSet',
    'ConcertInfoViewSet',
    'ConcertBidViewSet',
    'TicketViewSet',
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter


class ConcertInfoViewSet(viewsets.ModelViewSet):
    queryset = ConcertInfo.objects.all()
    serializer_class = ConcertInfoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ConcertInfoFilter


class ConcertBidViewSet(viewsets.ModelViewSet):
    queryset = ConcertBid.objects.all()
    serializer_class = ConcertBidSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ConcertBidFilter


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TicketFilter


def ticket_manager(request):
    c_info = enumerate([ConcertInfo.objects.get(id=id_)
                        for id_ in [4, 10, 16, 22, 28]])
    return render(request, 'ticket.jade', context={
        'c_info': c_info,
    })


def ticket_commit(request):
    '''
    Get parameters:
        cid: concert id
    '''
    cid = int(request.GET.get('cid', -1))

    c_info = enumerate([ConcertInfo.objects.get(id=id_)
                        for id_ in [4, 10, 16, 22, 28]])

    for bid in ConcertBid.objects.all():
        rank = 'a'
        for r in ['a', 'b', 'c', 'd', 'e']:
            if getattr(bid, '{}_rank'.format(r)) == '1':
                rank = r
                break

        price = getattr(bid, '{}_price'.format(rank)) - 100

        seat_num = 0
        line_num = randint(1, 20)
        for i in range(bid.qty):
            seat_num = seat_num + 1 if seat_num else randint(1, 13)
            region = '{} 區 {}行 {}號'.format(rank, line_num, seat_num)

            ticket = Ticket.objects.create(
                concert_info=bid.concert_info,
                region=region,
                price=price,
                token=str(uuid4()),
                state=1,
                user=bid.user,
            )

            # prepare data to block
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

        bid.delete()

    return render(request, 'ticket.jade', context={
        'c_info': c_info,
        'msg': 'Auction Complete',
        'cid': cid,
    })
